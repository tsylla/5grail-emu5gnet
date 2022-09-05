#!/bin/python3

import logging
from mininet.log import setLogLevel, info
from emuvim.dcemulator.net import DCNetwork
from emuvim.api.rest.rest_api_endpoint import RestApiEndpoint
import os
from mininet.link import Intf, TCLink
from mininet.node import Node
from mininet.util import quietRun
#from mininet.term import makeTerm


logging.basicConfig(level=logging.INFO)
setLogLevel('info')  # set Mininet loglevel
logging.getLogger('werkzeug').setLevel(logging.DEBUG)

class LinuxRouter(Node):
    def config( self, **params ):
        super( LinuxRouter, self).config( **params )
        # Enable forwarding on the router
        self.cmd( 'sysctl net.ipv4.ip_forward=1' )

    def terminate( self ):
        self.cmd( 'sysctl net.ipv4.ip_forward=0' )
        super( LinuxRouter, self ).terminate()

def create_topology():
    
    net = DCNetwork(monitor=False, enable_learning=False)

    info("***Creating emulated datacenters ****")

    defaultIP = '10.0.0.1/8'
    defaultExtIp = '15.0.0.3'
    defaultRoute = '10.0.0.1'

    iperf_server = net.addDocker("is1", volumes=["/home/wifi/mn-wifi-cnet-vimemu-install/db:/db"], 
                                ip="10.0.0.3/8", dimage='iperfserver:latest',
                                ports=[5201], port_bindings={5201:5201},publish_all_ports=True, 
                                defaultRoute="via %s"%defaultRoute)

    # gnb = net.addDocker("gnb", ip="10.0.0.2/8", volumes=['/home/wifi/mn-wifi-cnet-vimemu-install/ueransim:/ueransim'],
    #                 devices=['/dev/net/tun:/dev/net/tun'], dimage="ueransim:latest",
    #                 privileged=True, defaultRoute='via %s' %defaultRoute)

    router = net.addHost("r1", cls=LinuxRouter, ip=defaultIP, defaultRoute='via %s' %defaultExtIp)
    info("*** Adding switches for routing")
    #internal switch
    s3 = net.addSwitch('s3')
    #external switch
    s4 = net.addSwitch('s4')

    intfName = 'p2net'

    info("*** Connecting to intf %s"%intfName)
    Intf( intfName, node=s4)

    net.addLink(s3, router, cls=TCLink, bw=1000, intfName = 'r1-eth1', 
            params2={ 'ip' : defaultIP })
    net.addLink(s4, router, intfName = 'r1-eth2', cls=TCLink, bw=1000, params2={ 'ip' : '15.0.0.5/8'})


    #set iperf server and port as os environment variable
    os.environ['SERVER'] = '10.0.0.3'
    os.environ['PORT'] = '5201'
    os.environ['DEFAULT_ROUTE'] = defaultRoute

    dc1 = net.addDatacenter("dc1")
    dc2 = net.addDatacenter("dc2")
    dc3 = net.addDatacenter("dc3")

    net.addLink(s3, iperf_server, cls=TCLink, bw=1000)
    # net.addLink(s3, gnb, intfName = 'gnb-eth1', cls=TCLink, bw=10000)
    
    net.addLink(s3, dc1, cls=TCLink, delay="0ms", bw=1000)
    net.addLink(s3, dc2, cls=TCLink, delay="0ms", bw=1000)
    net.addLink(s3, dc3, cls=TCLink, delay="0ms", bw=1000)

    net.build()
    # add the command line interface endpoint to the emulated DC (REST API)
    rapi1 = RestApiEndpoint("0.0.0.0", 5001)
    rapi1.connectDCNetwork(net)
    rapi1.connectDatacenter(dc1)
    rapi1.connectDatacenter(dc2)
    rapi1.connectDatacenter(dc3)

    rapi1.start()

    net.start()

    info("*** Configuring %s interface"%intfName)

    config = quietRun( 'ifconfig %s up' %s4.name, shell=True)
    print(config)

    router.cmd("route add -net 11.0.0.0/8 gw 15.0.0.3")
    router.cmd("route add -net 10.45.0.0/8 gw 172.20.0.1")
    #dcmd="iperf3 -s -D -V --logfile /db/perf_data.txt"
    #makeTerm(iperf_server,"bash -c '%s"%dcmd)
    # dcmd = "bash -c './ueransim/run_gnb.sh'"
    # makeTerm(gnb,cmd=dcmd)
  #  gnb.cmd("ip route add 172.20.0.0/16 via 172.20.0.1")
    # route add -net 11.0.0.0/8 gw 12.0.0.2
    
    # quietRun( f'ip addr add {defaultExtIp}/8 dev {s4.name}', shell=True)
    # config = quietRun('ifconfig %s' %s4.name, shell=True)

    net.CLI()
    # when the user types exit in the CLI, we stop the emulator
    net.stop()
    
if __name__=="__main__":
    create_topology()

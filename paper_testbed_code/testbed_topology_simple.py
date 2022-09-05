# Copyright (c) 2018 SONATA-NFV, 5GTANGO and Paderborn University
# ALL RIGHTS RESERVED.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Neither the name of the SONATA-NFV, 5GTANGO, Paderborn University
# nor the names of its contributors may be used to endorse or promote
# products derived from this software without specific prior written
# permission.
#
# This work has also been performed in the framework of the 5GTANGO project,
# funded by the European Commission under Grant number 761493 through
# the Horizon 2020 and 5G-PPP programmes. The authors would like to
# acknowledge the contributions of their colleagues of the 5GTANGO
# partner consortium (www.5gtango.eu).
import logging
#import sys
from mininet.log import setLogLevel, info
from time import sleep

from emuvim.dcemulator.net import DCNetwork
from mininet.node import Controller, Node
#from mn_wifi.wmediumdConnector import interference
from mn_wifi.node import DCar
#from mn_wifi.sumo.runner import sumo

from emuvim.api.rest.rest_api_endpoint import RestApiEndpoint

logging.basicConfig(level=logging.DEBUG)
setLogLevel('info')  # set Mininet loglevel
logging.getLogger('werkzeug').setLevel(logging.DEBUG)
logging.getLogger('5gtango.llcm').setLevel(logging.DEBUG)

class LinuxRouter(Node):
    "A node with IP forwarding enabled and for operating as a Router"
    def __init__(self, name, **params):
        self.nat = True
        self.subnets = ["10.0.0.0/8"]
        super(LinuxRouter, self).__init__(name, **params)
    
    def config( self, **params ):
        super( LinuxRouter, self).config( **params )
        # Enable forwarding on the router
        self.cmd( 'sysctl net.ipv4.ip_forward=1' )

    def terminate( self ):
        self.cmd( 'sysctl net.ipv4.ip_forward=0' )
        super( LinuxRouter, self ).terminate()

def create_topology():

    # iperf3_server = net.addDocker('d1', ip='10.0.0.2', dimage="iperf3_server",
    #                 ports=[5201], port_bindings={5201:5201},publish_all_ports=True)
    # db_server = net.addDocker('d2', ip='10.0.0.3', dimage="mysql",
    #                 ports=[3306], port_bindings={3306:3306},publish_all_ports= True, 
    #                 environment={"USER": "user", "PASSWORD": "user" , "ROOT_PASSWORD": "root"})
    
    net = DCNetwork(monitor=False, enable_learning=True, controller=Controller)

    #initialize the hosts default ip address 
    defaultIP = '10.0.0.1/8'  
    router = net.addNode( 'r0', cls=LinuxRouter, ip=defaultIP )
    # IP address for r0-eth1
    info( '*** Adding router switch\n')
    s1 = net.addSwitch('s1')
    Intf( 'enp0s8', node=s1 )

    info( '*** Add hosts\n')
    h1 = net.addHost('h1', ip='0.0.0.0')

    info( '*** Add links\n')
    net.addLink(h1, s1)

    info( '*** Starting network\n')
    net.start()
    h1.cmdPrint('dhclient '+h1.defaultIntf().name)

    kwargs = {'ssid': '5G', 'mode': 'n','failMode': 'standalone', 
            'datapath': 'user', 'txpower': 55, 'range':350}
    # create rno and eno access points
    rno_ap1 = net.addAccessPoint('rno_ap1', mac='00:00:00:00:01:00', channel='6', position='350,550,0', **kwargs)
    rno_ap2 = net.addAccessPoint('rno_ap2', mac='00:00:00:00:02:00', channel='11', position='350,1050,0', **kwargs)
    rno_ap3 = net.addAccessPoint('rno_ap3', mac='00:00:00:00:03:00', channel='9', position='350,1600,0',**kwargs)

    eno1_ap1 = net.addAccessPoint('eno1_ap1', mac='00:00:00:00:04:00', channel='13', position='750,550,0',**kwargs)
    eno1_ap2 = net.addAccessPoint('eno1_ap2', mac='00:00:00:00:05:00', channel='6', position='750,1050,0', **kwargs)
    eno1_ap3 = net.addAccessPoint('eno1_ap3', mac='00:00:00:00:06:00', channel='9', position='750,1600,0', **kwargs)
    
    eno2_ap1 = net.addAccessPoint('eno2_ap1', mac='00:00:00:00:07:00', channel='1', position='1250,550,0',**kwargs)
    eno2_ap2 = net.addAccessPoint('eno2_ap2', mac='00:00:00:00:08:00', channel='6', position='1250,1050,0', **kwargs)
    eno2_ap3 = net.addAccessPoint('eno2_ap3', mac='00:00:00:00:09:00',channel='11', position='1250,1600,0', **kwargs)

    eno3_ap1 = net.addAccessPoint('eno3_ap1', mac='00:00:00:00:0A:00', channel='9', position='1750,550,0', **kwargs)
    eno3_ap2 = net.addAccessPoint('eno3_ap2', mac='00:00:00:00:0B:00',channel='6', position='1750,1050,0', **kwargs)
    eno3_ap3 = net.addAccessPoint('eno3_ap3', mac='00:00:00:00:0C:00',channel='13', position='1750,1600,0', **kwargs)    

    info("*** Creating nodes : Train and vehicles\n")
    tram_id = [3,10,41,59,79,89,108,131,150,172,191,215,241,256,285,300,328,356,371,408,418,444,481,498]
    kwargs2 = {'min_x':60, 'max_x':1200, 'min_y':100, 'max_y':1200, 'min_v':1, 'max_v':2,
             'mode':'n', 'dimage':"iperf_test_1:latest"}
    for id in range(0, 30):
        if id in tram_id:
            net.addDCar('tram%s' % id, cls=DCar, wlans=1, **kwargs2)
        else:
            net.addDCar('car%s' % id, cls=DCar, wlans=1, **kwargs2)

    #c0 = net.addController('c0')
    info("Adding controller ....")
    controllers = net.controllers
    c0 = controllers[0]

    info("Controller info : \n")
    info(c0)

    net.setPropagationModel(model="logDistance", exp=4.5)
    
    net.configureWifiNodes()

    #adding emulated datacenters or called PoP
    info("***Creating datacenters ****")
    rno_dc1 = net.addDatacenter("rno_dc1")
    rno_dc2 = net.addDatacenter("rno_dc2")
    rno_dc3 = net.addDatacenter("rno_dc3")
    
    eno1_dc1 = net.addDatacenter("eno1_dc1")
    eno1_dc2 = net.addDatacenter("eno1_dc2")
    eno1_dc3 = net.addDatacenter("eno1_dc3")

    eno2_dc1 = net.addDatacenter("eno2_dc1")
    eno2_dc2 = net.addDatacenter("eno2_dc2")
    eno2_dc3 = net.addDatacenter("eno2_dc3")

    eno3_dc1 = net.addDatacenter("eno3_dc1")
    eno3_dc2 = net.addDatacenter("eno3_dc2")
    eno3_dc3 = net.addDatacenter("eno3_dc3")

    info("**** Creating switch ****")
    rno_s = net.addSwitch('rnos1')
    eno1_s = net.addSwitch('eno1s1')
    eno2_s = net.addSwitch('eno2s1')
    eno3_s = net.addSwitch('eno3s1')
    core_s = net.addSwitch('cores1')
    
    info("**** Adding link to switch and ap and dc")
    # interconnect data centers, switches and access points
    
    net.addLink(rno_ap1, rno_s, ip="172.20.0.200/16", delay="5ms")
    net.addLink(rno_dc1, rno_s, ip="172.20.0.201/16", delay="10ms")
    net.addLink(rno_ap2, rno_s, ip="172.20.0.202/16", delay="5ms")
    net.addLink(rno_dc2, rno_s, ip="172.20.0.203/16")
    net.addLink(rno_ap3, rno_s, ip="172.20.0.204/16",delay="5ms")
    net.addLink(rno_dc3, rno_s, ip="172.20.0.205/16",delay="5ms")

    net.addLink(eno1_ap1, eno1_s,ip="172.20.0.206/16",delay="10ms")
    net.addLink(eno1_dc1, eno1_s, ip="172.20.0.207/16", delay="10ms")
    net.addLink(eno1_ap2, eno1_s, ip="172.20.0.208/16", delay="15ms")
    net.addLink(eno1_dc2, eno1_s, ip="172.20.0.209/16",delay="10ms")
    net.addLink(eno1_ap3, eno1_s, ip="172.20.0.210/16",delay="15ms")
    net.addLink(eno1_dc3, eno1_s, ip="172.20.0.211/16",delay="10ms")

    net.addLink(eno2_ap1, eno2_s, ip="172.20.0.212/16",delay="10ms")
    net.addLink(eno2_dc1, eno2_s, ip="172.20.0.213/16",delay="10ms")
    net.addLink(eno2_ap2, eno2_s, ip="172.20.0.214/16", delay="15ms")
    net.addLink(eno2_dc2, eno2_s, ip="172.20.0.215/16",delay="10ms")
    net.addLink(eno2_ap3, eno2_s, ip="172.20.0.216/16", delay="15ms")
    net.addLink(eno2_dc3, eno2_s, ip="172.20.0.217/16",delay="10ms")

    net.addLink(eno3_ap1, eno3_s, ip="172.20.0.218/16",delay="10ms")
    net.addLink(eno3_dc1, eno3_s, ip="172.20.0.219/16",delay="10ms")
    net.addLink(eno3_ap2, eno3_s, ip="172.20.0.220/16",delay="15ms")
    net.addLink(eno3_dc2, eno3_s, ip="172.20.0.221/16", delay="10ms")
    net.addLink(eno3_ap3, eno3_s, ip="172.20.0.222/16", delay="15ms")
    net.addLink(eno3_dc3, eno3_s, ip="172.20.0.223/16",delay="10ms")

    net.addLink(rno_s, core_s,ip="172.20.0.224/16")
    net.addLink(eno1_s, core_s,ip="172.20.0.225/16")
    net.addLink(eno2_s, core_s,ip="172.20.0.226/16")
    net.addLink(eno3_s, core_s, ip="172.20.0.227/16")

    #Start the controller and access points 
    #link the controller the access points
    c0.start()
    for gNb in net.aps:
        gNb.start([c0])

    #Assign address IP to the train and cars
    #For more simplicity, we suppose that all nodes are sharing
    #the same logical network
    # for id, car in enumerate(net.cars):
    #     car.setIP('172.20.0.{}/16'.format(+20+id+1),
    #     intf='{}'.format(car.wintfs[0].name))

    """plot graph"""
    net.plotGraph(max_x=2000, max_y=2000)

    net.setMobilityModel(time=0, model='RandomDirection',
                         max_x=1500, max_y=1500, seed=20)

    # add the command line interface endpoint to the emulated DC (REST API)
    rapi1 = RestApiEndpoint("0.0.0.0", 5001)
    rapi1.connectDCNetwork(net)
    rapi1.connectDatacenter(rno_dc1)
    rapi1.connectDatacenter(rno_dc2)
    rapi1.connectDatacenter(rno_dc3)
    rapi1.connectDatacenter(eno1_dc1)
    rapi1.connectDatacenter(eno1_dc2)
    rapi1.connectDatacenter(eno1_dc3)
    rapi1.connectDatacenter(eno2_dc1)
    rapi1.connectDatacenter(eno2_dc2)
    rapi1.connectDatacenter(eno2_dc3)
    rapi1.connectDatacenter(eno3_dc1)
    rapi1.connectDatacenter(eno3_dc2)
    rapi1.connectDatacenter(eno3_dc3)
    rapi1.start()
    
    # start the emulation and enter interactive CLI
 
    
    # info('Connecting to traci - sumo')
    #     # exec_order: Tells TraCI to give the current
    # # client the given position in the execution order.
    # # We may have to change it from 0 to 1 if we want to
    # # load/reload the current simulation from a 2nd client
    # net.useExternalProgram(program=sumo, port=8813,
    #                        config_file='Grande_Map/osm.sumocfg',
    #                        extra_params=["--start --delay 200"],
    #                        clients=1, exec_order=0)
    
    info("**** Starting network and connecting to traci")
    
    net.build()
    net.start()
    
    for id, car in enumerate(net.cars):
        cmd_to_run = 'iw dev {} connect 5G'.format(car.wintfs[0].name)
        car.cmd(cmd_to_run)
        sleep(0.1)        
        car.setIP('172.20.0.{}/16'.format(+20+id+1),
        intf='{}'.format(car.wintfs[0].name))
        
        cmd_wifi_info = "bash -c 'iw dev + {} link'".format(car.wintfs[0].name)

    net.CLI()
    # when the user types exit in the CLI, we stop the emulator
    net.stop()

def main():
    create_topology()

if __name__ == '__main__':
    main()

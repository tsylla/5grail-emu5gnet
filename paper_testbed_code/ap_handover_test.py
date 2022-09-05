import sys

from emuvim.api.rest.rest_api_endpoint import RestApiEndpoint
from emuvim.dcemulator.net import DCNetwork
from mininet.node import Controller, RemoteController, OVSKernelSwitch
from mininet.log import setLogLevel, info
from mn_wifi.node import UserAP
from mn_wifi.cli import CLI
from mn_wifi.node import OVSAP
from mn_wifi.link import wmediumd
from mn_wifi.wmediumdConnector import interference


def topology(args):
    "Create a network."
    #net = Mininet_wifi(controller=Controller, accessPoint=UserAP,
    #                   link=wmediumd, wmediumd_mode=interference)

    #c0 = RemoteController('c0', ip='127.0.0.1', port=6653, protocols="OpenFlow13")

    net = DCNetwork(monitor=False, enable_learning=True, controller=RemoteController, link=wmediumd,
                    wmediumd_mode=interference)

    info("*** Creating nodes\n")
    net.addStation('sta1', position='15,20,0', bgscan_threshold=-60,
                   s_inverval=5, l_interval=10, bgscan_module="simple")
    net.addStation('sta2', position='125,120,0', bgscan_threshold=-60,
                   s_interval=5,l_interval=10, bgscan_moduke="simple")

    ap1 = net.addAccessPoint('ap1', mac='00:00:00:00:00:01', ssid="handover",
                             mode="g", channel="1", passwd='123456789a',
                             encrypt='wpa2', position='10,30,0')
 #   ap2 = net.addAccessPoint('ap2', mac='00:00:00:00:00:02', ssid="handover",
 #                            mode="g", channel="6", passwd='123456789a',
 #                            encrypt='wpa2', position='60,30,0')
    ap3 = net.addAccessPoint('ap3', mac='00:00:00:00:00:03', ssid="handover",
                             mode="g", channel="1", passwd='123456789a',
                             encrypt='wpa2', position='120,100,0')

#    c0 = net.addController(c0)

    info("*** Configuring Propagation Model\n")
    net.setPropagationModel(model="logDistance", exp=1)

    s1 = net.addSwitch("s1")
    s2 = net.addSwitch("s2")
    s3 = net.addSwitch("s3")
    s4 = net.addSwitch("s4")
    s5 = net.addSwitch("s5")
    dc1 = net.addDatacenter("dc1")

    info("*** Creating links\n")
    #net.addLink(ap1, ap2)
    #net.addLink(ap2, ap3)

    net.addLink(ap1,s1)
  #  net.addLink(ap2,s2)
    net.addLink(ap3,s3)
    net.addLink(dc1,s4)
    net.addLink(s5,s1)
    net.addLink(s5,s2)
    net.addLink(s5,s3)
    net.addLink(s5,s4)

    info("*** Configuring wifi nodes\n")
    net.configureWifiNodes()

    """plot graph"""
    net.plotGraph(max_x=200, max_y=200)

    info("*** Starting network\n")

    net.build()

    #c0.start()
    #s1.start([c0])
    #ap1.start([c0])
    #ap2.start([c0])
    #ap3.start([c0])

    rapi1 = RestApiEndpoint("0.0.0.0", 5001)
    rapi1.connectDCNetwork(net)

    rapi1.connectDatacenter(dc1)
    net.start()
#    net.pingAll()
    info("*** Running CLI\n")
    CLI(net)

    info("*** Stopping network\n")
    net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    topology(sys.argv)
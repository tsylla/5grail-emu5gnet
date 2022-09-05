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
import sys
from mininet.log import setLogLevel, info
import testbed_utils as tu

from emuvim.dcemulator.net import DCNetwork
from mininet.node import Controller
from mn_wifi.link import wmediumd
from mn_wifi.wmediumdConnector import interference
from mn_wifi.sumo.runner import sumo
#from mininet.link import TCLink
from mn_wifi.node import UserAP

from emuvim.api.rest.rest_api_endpoint import RestApiEndpoint

import os, sys

logging.basicConfig(level=logging.DEBUG)
setLogLevel('info')  # set Mininet loglevel
#logging.getLogger('werkzeug').setLevel(logging.DEBUG)
#logging.getLogger('5gtango.llcm').setLevel(logging.DEBUG)


def create_topology():

    # iperf3_server = net.addDocker('d1', ip='10.0.0.2', dimage="iperf3_server",
    #                 ports=[5201], port_bindings={5201:5201},publish_all_ports=True)
    # db_server = net.addDocker('d2', ip='10.0.0.3', dimage="mysql",
    #                 ports=[3306], port_bindings={3306:3306},publish_all_ports= True, 
    #                 environment={"USER": "user", "PASSWORD": "user" , "ROOT_PASSWORD": "root"})


    ac_method = 'ssf'
    if '-llf' in sys.argv:
        ac_method = 'llf'

    trains_file = "good_map/osm.rail.trips.xml"
    access_points_file = "ap_names_positions.csv"
    cars_file = "good_map/osm.passenger.trips.xml"

    # net = DCNetwork(monitor=False, enable_learning=True, controller=Controller,
    #                 link=wmediumd, wmediumd_mode=interference, ac_method=ac_method)
    net = DCNetwork(monitor=False, enable_learning=True, controller=Controller, ac_method=ac_method)
    kwargs = {'txpower':'6dBm','range': 150,'ssid':'wifi'}
    #'ssid': 'new-ssid', 'mode': 'n', 'band': '40',

    # info("Loading trains and cars informations")
    # trains_ids = tu.getIdFromXml(trains_file)
    # cars_ids = tu.getIdFromXml(cars_file)

    info("*** Creating nodes : Train and vehicles\n")

    # info("Trains list :")
    # print(trains_ids)
    # info("Cars list")
    # print(cars_ids)
    kwargs2 = {'bgscan_threshold':-50,'s_inverval':1, 'l_interval':4, 'bgscan_module':'simple'}

    # for id in range(len(trains_ids)):
    for id in range(0,30):
        #train_id = 'train%s'%trains_ids[id]
        net.addCar('car%02d'%(id+1),**kwargs2)
        #net.addCar(train_id,**kwargs2)

    for id in range(0,30):
        car_id = 'car%02d'%(id+1)
        net.addCar(car_id, **kwargs2)        
    

    info('*** List of created car and trains : ')
    print(net.cars)

    info("***Creating emulated datacenters ****")

    dc1 = net.addDatacenter("dc1")
    dc2 = net.addDatacenter("dc2")
    dc3 = net.addDatacenter("dc3")
    dc4 = net.addDatacenter("dc4")
    dc5 = net.addDatacenter("dc5")
    dc6 = net.addDatacenter("dc6")
    dc7 = net.addDatacenter("dc7")
    dc8 = net.addDatacenter("dc8")

    info("**** Creating switch ****")
    s1 = net.addSwitch("s1")
    s2 = net.addSwitch("s2")
    s3 = net.addSwitch("s3")
    s4 = net.addSwitch("s4")
    s5 = net.addSwitch("s5")
    s6 = net.addSwitch("s6")
    s7 = net.addSwitch("s7")
    s8 = net.addSwitch("s8")

    c1 = net.addSwitch('c1')
    c2 = net.addSwitch('c2')
    # create access points
    info("Access points creation")
    #access_points = tu.get_access_point_names(access_points_file)
    ap_1 = net.addAccessPoint('ap_1', channel=6, position='484.85,1909.24,15',
                              mac="00:00:00:11:00:01",**kwargs)

    ap_2 = net.addAccessPoint('ap_2', channel=11, position='595.86,1929.33,15',
                              mac="00:00:00:11:00:02", **kwargs)

    ap_3 = net.addAccessPoint('ap_3', channel=1, position='751.26,1964.21,15',
                              mac="00:00:00:11:00:03", **kwargs)

    ap_4 = net.addAccessPoint('ap_4', channel=13, position='901.38,1993.81,15',
                              mac="00:00:00:11:00:04", **kwargs)

    ap_5 = net.addAccessPoint('ap_5', channel=6, position='1063.13,2027.64,15',
                              mac="00:00:00:11:00:05", **kwargs)

    ap_6 = net.addAccessPoint('ap_6', channel=11, position='1231.18,2061.60,15',
                              mac="00:00:00:11:00:06", **kwargs)

    ap_7 = net.addAccessPoint('ap_7', channel=13, position='1459.36,2098.43,15',
                              mac="00:00:00:11:00:07", **kwargs)

    ap_8 = net.addAccessPoint('ap_8', channel=1, position='1662.75,2143.74,15',
                              mac="00:00:00:11:00:08", **kwargs)

    ap_9 = net.addAccessPoint('ap_9', channel=6, position='1876.11,2184.11,15',
                              mac="00:00:00:11:00:09", **kwargs)

    ap_10 = net.addAccessPoint('ap_10', channel=11, position='2100.04,2229.28,15',
                              mac="00:00:00:11:00:10", **kwargs)

    ap_11 = net.addAccessPoint('ap_11', channel=1, position='2273.35,2260.56,15',
                              mac="00:00:00:11:00:11", **kwargs)

    ap_12 = net.addAccessPoint('ap_12', channel=13, position='2459.97,2289.58,15',
                              mac="00:00:00:11:00:12", **kwargs)
    ap_13 = net.addAccessPoint('ap_13', channel=6, position='2606.27,2309.86,15',
                              mac="00:00:00:11:00:13", **kwargs)
    ap_14 = net.addAccessPoint('ap_14', channel=11, position='2746.83,2316.27,15',
                              mac="00:00:00:11:00:14", **kwargs)
    ap_15 = net.addAccessPoint('ap_15', channel=1, position='2931.61,2347.29,15',
                              mac="00:00:00:11:00:15", **kwargs)
    ap_16 = net.addAccessPoint('ap_16', channel=13, position='2974.53,2485.56,15',
                              mac="00:00:00:11:00:16", **kwargs)
    ap_17 = net.addAccessPoint('ap_17', channel=6, position='3244.08,2538.74,15',
                              mac="00:00:00:11:00:17", **kwargs)

    print("Access points loading complete \n.")

    info("Adding controller ....")
    #c0 = net.addController('c0')
    controllers = net.controllers
    c0 = controllers[0]

    info("Controller info : \n")
    info(c0)
    #net.setPropagationModel(model="logDistance", exp=5)

    #adding emulated datacenters or called PoP
    net.configureWifiNodes()
    info("**** Adding link to switch and ap and dc")
    net.addLink(s1, ap_1)
    net.addLink(s1, ap_3)
    net.addLink(s1, dc1)

    net.addLink(s2,ap_2)
    net.addLink(s2,ap_4)
    net.addLink(s2, dc5)

    net.addLink(s3, ap_5)
    net.addLink(s3, ap_7)
    net.addLink(s3, dc2)

    net.addLink(s4, ap_6)
    net.addLink(s4, ap_8)
    net.addLink(s4, dc6)

    net.addLink(s5, ap_9)
    net.addLink(s5, ap_11)
    net.addLink(s5, dc3)

    net.addLink(s6, ap_10)
    net.addLink(s6, ap_12)
    net.addLink(s6, dc7)

    net.addLink(s7, ap_13)
    net.addLink(s7, ap_15)
    net.addLink(s7, ap_17)
    net.addLink(s7, dc4)

    net.addLink(s8, ap_14)
    net.addLink(s8, ap_16)
    net.addLink(s8, dc8)

    net.addLink(c1, s1)
    net.addLink(c1, s3)
    net.addLink(c1, s5)
    net.addLink(c1, s7)
    net.addLink(c2, s2)
    net.addLink(c2, s4)
    net.addLink(c2, s6)
    net.addLink(c2, s8)
    net.addLink(c1, c2)


    """plot graph"""
    net.plotGraph(min_x=0, min_y=0, max_x=3000, max_y=3000)

    #Start the controller and access points  
    #link the controller the access points
    net.build()
    c0.start()
    for ap in net.aps:
        ap.start([c0])

    #Assign address IP to the train and cars
    #For more simplicity, we suppose that all nodes are sharing
    #the same logical network
    for id, car in enumerate(net.cars):
        car.setIP('10.0.0.{}/16'.format(id+4+1), intf='{}'.format(car.wintfs[0].name))
         #car.setRange(150)
         # car.setTxPower(49)
         # car.setAntennaGain(10)

    # add the command line interface endpoint to the emulated DC (REST API)
    rapi1 = RestApiEndpoint("0.0.0.0", 5001)
    rapi1.connectDCNetwork(net)

    rapi1.connectDatacenter(dc1)
    rapi1.connectDatacenter(dc2)
    rapi1.connectDatacenter(dc3)
    rapi1.connectDatacenter(dc4)
    rapi1.connectDatacenter(dc5)
    rapi1.connectDatacenter(dc6)
    rapi1.connectDatacenter(dc7)
    rapi1.connectDatacenter(dc8)
    
    rapi1.start()

    #import pdb
    #pdb.set_trace()
    info("**** Starting network and connecting to traci")
    info('Connecting to traci - sumo')
    #     # exec_order: Tells TraCI to give the current
    # # client the given position in the execution order.
    # # We may have to change it from 0 to 1 if we want to
    # # load/reload the current simulation from a 2nd client
    nodes = net.cars + net.aps
    # import pdb
    # pdb.set_trace()
    net.useExternalProgram(program=sumo, port=8813,
                           config_file='good_map/osm.sumocfg',
                           extra_params=["--start --delay 500"],
                            clients=1, exec_order=0)


    info('****---- Nodes and aps list :')
    print(nodes)
    #net.telemetry(nodes=nodes, data_type='rssi')
    #net.telemetry(nodes=nodes, data_type='position')

    net.start()
    
    net.CLI()
    # when the user types exit in the CLI, we stop the emulator
    net.stop()


if __name__ == '__main__':
    create_topology()

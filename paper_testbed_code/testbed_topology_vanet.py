#!/bin/python3

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

from ipaddress import ip_address
import logging
import sys
from mininet.log import setLogLevel, info
import testbed_utils as tu
import time

from emuvim.dcemulator.net import DCNetwork
from mininet.node import Controller, RemoteController
from mn_wifi.node import OVSKernelAP
from mn_wifi.link import wmediumd
from mn_wifi.cli import CLI
from mn_wifi.wmediumdConnector import interference
from mn_wifi.sumo.runner import sumo
#from mininet.link import TCLink

from emuvim.api.rest.rest_api_endpoint import RestApiEndpoint

logging.basicConfig(level=logging.DEBUG)
setLogLevel('info')  # set Mininet loglevel

def create_topology():

    trains_file = "good_map/osm.rail.trips.xml"
    access_points_file = "ap_names_positions.csv"
    cars_file = "good_map/osm.passenger.trips.xml"



    # net = DCNetwork(monitor=False, enable_learning=True, controller=Controller,
    #                 link=wmediumd, wmediumd_mode=interference, ac_method=ac_method)
    net = DCNetwork(monitor=False, enable_learning=True, link=wmediumd, wmediumd_mode=interference)

    kwargs = {'ssid':'wifi','encrypt': 'wpa2', 'mode':'n',
        'passwd': '123456789a','protocols':'OpenFlow13',
        'txpower':'16dBm','range': 250}

    info("Loading trains and cars informations")
    trains_ids = tu.getIdFromXml(trains_file,"trip")
    cars_ids = tu.getIdFromXml(cars_file, "trip")

    info("*** Creating nodes : Train and vehicles\n")

    # info("Trains list :")
    # print(trains_ids)
    # info("Cars list")
    # print(cars_ids)
    kwargs2 = {'bgscan_threshold':-70,'s_inverval':3, 'l_interval':10, 'bgscan_module':'simple'}
    h1 = net.addHost("h1", ip="10.0.0.1/8")
    h2 = net.addHost("h2", ip="10.0.0.2/8")
    h3 = net.addHost("h3", ip="10.0.0.3/8")
    h4 = net.addHost("h4", ip="10.0.0.4/8")
    # # for id in range(len(trains_ids)):
    
    for id in range(1,20):
        train_id = 't%s'%trains_ids[id]
        ip_address = '10.0.0.{}/8'.format(id+10+1)
        net.addCar(train_id, ip=ip_address, encrypt=['wpa2', '123456789a'], **kwargs2)
        
    #     #net.addCar(train_id,**kwargs2)

    # for id in range(1,10):
    #     car_id = 'c%s'%cars_ids[id]
    #     net.addCar(car_id, wlans=1, encrypt=['wpa2', '123456789a'],**kwargs2)

    # create access points
    info("Access points creation")
    #access_points = tu.get_access_point_names(access_points_file)
    ap_1 = net.addAccessPoint('ap_1', channel=6, position='484,1909,0',
                              mac="00:00:00:11:00:01",**kwargs)

    ap_2 = net.addAccessPoint('ap_2', channel=11, position='595,1929,0',
                              mac="00:00:00:11:00:02", **kwargs)

    ap_3 = net.addAccessPoint('ap_3', channel=1, position='751,1964,0',
                              mac="00:00:00:11:00:03", **kwargs)

    ap_4 = net.addAccessPoint('ap_4', channel=13, position='901,1993,0',
                              mac="00:00:00:11:00:04", **kwargs)

    ap_5 = net.addAccessPoint('ap_5', channel=6, position='1063,2027,0',
                              mac="00:00:00:11:00:05", **kwargs)

    ap_6 = net.addAccessPoint('ap_6', channel=11, position='1231,2061,0',
                              mac="00:00:00:11:00:06", **kwargs)

    ap_7 = net.addAccessPoint('ap_7', channel=13, position='1459,2098,0',
                              mac="00:00:00:11:00:07", **kwargs)

    ap_8 = net.addAccessPoint('ap_8', channel=1, position='1662,2143,0',
                              mac="00:00:00:11:00:08", **kwargs)

    ap_9 = net.addAccessPoint('ap_9', channel=6, position='1876,2184,0',
                              mac="00:00:00:11:00:09", **kwargs)

    ap_10 = net.addAccessPoint('ap_10', channel=11, position='2100,2229,0',
                              mac="00:00:00:11:00:10", **kwargs)

    ap_11 = net.addAccessPoint('ap_11', channel=1, position='2273,2260,0',
                              mac="00:00:00:11:00:11", **kwargs)

    ap_12 = net.addAccessPoint('ap_12', channel=13, position='2459,2289,0',
                              mac="00:00:00:11:00:12", **kwargs)
    ap_13 = net.addAccessPoint('ap_13', channel=6, position='2606,2309,0',
                              mac="00:00:00:11:00:13", **kwargs)
    ap_14 = net.addAccessPoint('ap_14', channel=11, position='2746,2316,0',
                              mac="00:00:00:11:00:14", **kwargs)
    ap_15 = net.addAccessPoint('ap_15', channel=1, position='2931,2347,0',
                              mac="00:00:00:11:00:15", **kwargs)
    ap_16 = net.addAccessPoint('ap_16', channel=13, position='2974,2485,0',
                              mac="00:00:00:11:00:16", **kwargs)
    ap_17 = net.addAccessPoint('ap_17', channel=6, position='3244,2538,0',
                              mac="00:00:00:11:00:17", **kwargs)

    print("Access points loading complete \n.")

    # info("*** Configuring Propagation Model\n")
    net.setPropagationModel(model="logDistance", exp=2.8)

    #controllers = net.controllers
    #c0 = controllers[0]
    #c0 = net.addController('c0', port=6653, ip='127.0.0.1')
    #c0 = RemoteController('c0', ip='127.0.0.1', port=6653, protocols="OpenFlow13")
    #net.addController(c0)
    info("Adding controller ....")
    #controllers = net.controllers
    #c0 = controllers[0]

    #info("Controller info : \n")
    #info(c0)

    #adding emulated datacenters or called PoP
    net.configureWifiNodes()

    info("***Creating emulated datacenters ****")

    dc1 = net.addDatacenter("dc1")
    dc2 = net.addDatacenter("dc2")
    dc3 = net.addDatacenter("dc3")
    # dc4 = net.addDatacenter("dc4")
    # dc5 = net.addDatacenter("dc5")
    # dc6 = net.addDatacenter("dc6")
    # dc7 = net.addDatacenter("dc7")
    # dc8 = net.addDatacenter("dc8")

    info("**** Adding link to switch and ap and dc")


    # net.addLink(h1, ap_1)
    # net.addLink(h2, ap_6)
    # net.addLink(h3, ap_17)
    # net.addLink(ap_1, ap_2)
    # net.addLink(ap_2, ap_3)
    # net.addLink(ap_3, ap_4)
    # net.addLink(ap_4, ap_5)
    # net.addLink(ap_5, ap_6)
    # net.addLink(ap_6, ap_7)
    # net.addLink(ap_7, ap_8)
    # net.addLink(ap_8, ap_9)
    # net.addLink(ap_9, ap_10)
    # net.addLink(ap_10, ap_11)
    # net.addLink(ap_11, ap_12)
    # net.addLink(ap_12, ap_13)
    # net.addLink(ap_13, ap_14)
    # net.addLink(ap_14, ap_15)
    # net.addLink(ap_15, ap_16)
    # net.addLink(ap_16, ap_17)
    net.addLink(h1, ap_1)
    net.addLink(dc1, ap_1)
    #net.addLink(dc1, ap_1)
    # net.addLink(dc5, ap_2)
    net.addLink(h2, ap_2)
    net.addLink(dc2, ap_5)
    net.addLink(h3, ap_5)
    # net.addLink(dc6, ap_11)
    net.addLink(h4, ap_17)
    net.addLink(dc2, ap_17)
    net.addLink(dc3, ap_9)
    # net.addLink(dc7, ap_10)
    # net.addLink(dc8, ap_14)
    #net.addLink(dc4, ap_13)
    #net.addLink(dc1, ap_3)

    net.addLink(ap_1, ap_2)
    

    net.addLink(ap_2, ap_3)
    net.addLink(ap_3, ap_4)
    net.addLink(ap_4, ap_5)
    net.addLink(ap_5, ap_6)
    net.addLink(ap_6, ap_7)
    net.addLink(ap_7, ap_8)
    
    net.addLink(ap_8, ap_9)
    net.addLink(ap_9, ap_10)

    net.addLink(ap_10, ap_11)
    net.addLink(ap_11, ap_12)
    net.addLink(ap_12, ap_13)

    net.addLink(ap_13, ap_14)

    net.addLink(ap_14, ap_15)
    net.addLink(ap_15, ap_16)
    net.addLink(ap_16, ap_17)
    #net.addLink(dc5, ap_4)
    
   # net.addLink(dc2, ap_6)
   # net.addLink(dc2, ap_7)
    
    
   # net.addLink(dc3, ap_11)
    
   # net.addLink(dc7, ap_12)
    
    
   # net.addLink(dc4, ap_15)
    #net.addLink(dc8, ap_16)
    #net.addLink(dc4, ap_17)
    
    # # add the command line interface endpoint to the emulated DC (REST API)
    rapi1 = RestApiEndpoint("0.0.0.0", 5001)
    rapi1.connectDCNetwork(net)

    rapi1.connectDatacenter(dc1)
    rapi1.connectDatacenter(dc2)
    rapi1.connectDatacenter(dc3)
    # rapi1.connectDatacenter(dc4)
    # rapi1.connectDatacenter(dc5)
    # rapi1.connectDatacenter(dc6)
    # rapi1.connectDatacenter(dc7)
    # rapi1.connectDatacenter(dc8)
    
    rapi1.start()

    #import pdb
    #pdb.set_trace()
    info("**** Starting network and connecting to traci")
    info('Connecting to traci - sumo')
    #     # exec_order: Tells TraCI to give the current
    # # client the given position in the execution order.
    # # We may have to change it from 0 to 1 if we want to
    # # load/reload the current simulation from a 2nd client

    net.useExternalProgram(program=sumo, port=8813,
                           config_file='good_map/osm.sumocfg',
                           extra_params=["--start --delay 1000"],
                            clients=1, exec_order=0)

    net.build()
    # """plot graph"""
    # net.plotGraph(min_x=0, min_y=0, max_x=3000, max_y=3000)

    #Start the controller and access points  
    #link the controller the access points
    # c0.start()
    # for ap in net.aps:
    #     ap.start([c0])

    #Assign address IP to the train and cars
    #For more simplicity, we suppose that all nodes are sharing
    # #the same logical network
    # for id, car in enumerate(net.cars):
    #     car.setIP('10.0.0.{}/8'.format(id+10+1), intf='{}'.format(car.wintfs[0].name))

    # Track the position of the nodes
    nodes = net.cars + net.aps
    # info("**** Node : .............................************----------------------")
    # print(nodes)
    net.telemetry(nodes=nodes, data_type='position',
                  min_x=500, min_y=500,
                  max_x=3000, max_y=3000)

    # info("**** Launching ping Ping")
    # timer_debut = time.perf_counter()
    # while True :
    #     timer_nouv = time.perf_counter()
    #     elapsed = timer_nouv - timer_debut
    #     if elapsed >= 5 :
    #         for c in net.cars:
    #             c.cmd(car.cmd("ping -c 10 {} &".format("10.0.0.1")))
    #         break

    net.start()
#    net.pingAll()

    info("*** Running CLI\n")
    CLI(net)
    # when the user types exit in the CLI, we stop the emulator
    net.stop()


if __name__ == '__main__':
    create_topology()

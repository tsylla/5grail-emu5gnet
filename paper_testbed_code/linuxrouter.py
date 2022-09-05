from mininet.net import Mininet
from mininet.log import lg, info
from mininet.node import Node
from mininet.topolib import TreeTopo
from mininet.topo import Topo
from subprocess import call

class LinuxRouter(Node):
    "A node with IP forwarding enabled and for operating as a Router"
    def __init__(self, name, **params):
        self.nat = True
        self.subnets = ["10.0.0.0/8"]
        super(LinuxRouter, self).__init__(name, **params)
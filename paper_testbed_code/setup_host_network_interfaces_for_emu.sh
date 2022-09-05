#!/bin/bash

sudo ip tuntap add tapemu mode tap
sudo ip link set dev tapemu up

sudo ip link add dev p1net type veth peer name p1netbr
sudo ip link set dev p1netbr up

sudo ip link add dev p2net type veth peer name p2netbr
sudo ip link set dev p2netbr up

sudo ip link add bremu type bridge

sudo ip link set tapemu master bremu
sudo ip link set p1netbr master bremu
sudo ip link set p2netbr master bremu

sudo ip addr add 15.0.0.1/29 dev bremu
sudo ip addr add 15.0.0.2/29 dev p1net
sudo ip addr add 15.0.0.3/29 dev p2net

sudo ip link set bremu up
sudo ip link set p1net up
sudo ip link set p2net up

sudo ip route add 11.0.0.0/8 via 15.0.0.4
sudo ip route add 10.0.0.0/8 via 15.0.0.5

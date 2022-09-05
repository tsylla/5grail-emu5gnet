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

ip tuntap add name ogstun mode tun
ip addr add 10.45.0.1/16 dev ogstun
ip addr add 2001:230:cafe::1/48 dev ogstun
ip link set ogstun up

sudo iptables -t nat -A POSTROUTING -s 10.45.0.0/16 ! -o ogstun -j MASQUERADE 
sudo ip6tables -t nat -A POSTROUTING -s 2001:db8:cafe::/48 ! -o ogstun -j MASQUERADE

sudo iptables-restore < iptables-rules

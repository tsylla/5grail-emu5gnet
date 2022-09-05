#!/bin/sh
ifconfig eth0 0
ifconfig gnb1-eth0 0

ip addr add 172.20.0.3/16 dev eth0
ip addr add 11.0.0.2/8 dev gnb1-eth0
ip addr add 11.0.0.3/8 dev gnb1-eth0

ip link set eth0 up
ip link set gnb1-eth0 up

ip route add 15.0.0.0/8 via 11.0.0.1
ip route add 10.0.0.0/8 via 11.0.0.1
ip route del default
ip route add default via 172.20.0.1

ping -c 10 172.20.0.2

cd ueransim/UERANSIM/
build/nr-gnb -c 'config/open5gs-gnb.yaml'

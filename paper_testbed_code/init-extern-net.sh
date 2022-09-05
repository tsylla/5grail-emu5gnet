#!/bin/zsh

sudo ip link add dev dummy1 type dummy   

sudo ip link set dummy1 up              

sudo ip a add 10.0.0.1/8 dev dummy1  

sudo iptables -A FORWARD -i dummy1 -j ACCEPT           


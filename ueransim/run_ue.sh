#!/bin/sh

#ip route add default via 11.0.0.1

sleep 5

ping -c 40 11.0.0.2

cd /ueransim/UERANSIM/
build/nr-ue -c 'config/t'$1'-ue.yaml'

ping -I uesimtun0 -c 30 10.45.0.1 > 't'$1'-ue-pingtocore.txt'
#ip route add default via 10.45.0.1
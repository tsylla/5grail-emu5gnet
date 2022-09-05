#!/usr/bin/zsh

#run the testbed code
qterminal -e ./testbed_topology_vanet_routing.py &
qterminal -e ./datacenter_emulator.py &
qterminal -e ./orchestrator_start.sh &

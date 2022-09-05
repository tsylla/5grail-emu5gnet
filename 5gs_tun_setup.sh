ip tuntap add name ogstun mode tun
ip addr add 10.45.0.1/16 dev ogstun
ip addr add 2001:230:cafe::1/48 dev ogstun
ip link set ogstun up

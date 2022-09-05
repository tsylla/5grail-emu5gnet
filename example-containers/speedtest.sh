#!/bin/sh

ip route del default
ip route add default via ${DEFAULT_ROUTE} 

while :
do
    python3 speedtest.py ${SERVER} ${PORT} '/db/testbed_db.db'
    sleep 10
done
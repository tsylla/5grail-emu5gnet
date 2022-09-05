#!/bin/bash

#touch /var/log/cron.log

#python3 bandwidth_test.py '172.17.0.2' '5201' '172.18.0.2'

python3 bandwidth_test.py @IPERF_SERVER@ @IPERF_PORT@ @DB_SERVER@
import subprocess as sp
import sys
import time as t

def check_wifi_connectivity(hostname):
    cmd_to_run = f"iw dev {hostname}-wlan0 link"

    debut = t.perf_counter()

    while True:
        ecoule = t.perf_counter() - debut

        if ecoule > 1 :
            output = sp.getoutput(cmd_to_run)
            print("host connection status : \n")
            print(output)
            if output.find("Not connected.") == -1 :
                return True
            else :
                debut = t.perf_counter()

if __name__=="__main__":
    hostname = sys.argv[1]

    if check_wifi_connectivity(hostname):
        #build curl request

        data = '{"vnf_name":"vnf_'+hostname+'","image":"vnf","volume":"/home/wifi/db:/db", "cpu_period":"10000","cpu_quota":"2000","mem_limit":"20m","node":"'+hostname+'"}'
        cmd = "curl -d '"+ data  + "' -X POST http://15.0.0.1:8899/vnf/api/start" + " -H \"Content-Type: application/json\" "
        print("cmd : "+cmd)
        output = sp.getoutput(cmd)
        print(output)
        t.sleep(5)

        exit(0)
        
    
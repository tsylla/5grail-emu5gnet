import subprocess as sp
import sys
import time as t

def check_wifi_connectivity(hostname):
    cmd_to_run = f"iw dev {hostname}-wlan0 link"

    start = t.perf_counter()

    while True:
        elapsed = t.perf_counter() - start

        if elapsed > 1 :
            output = sp.getoutput(cmd_to_run)
            print("host connection status : \n")
            print(output)
            # if output.find("Not connected.") == -1 :
            #     return True
            # else :
            start = t.perf_counter()

if __name__=="__main__":
    hostname = sys.argv[1]
    iperf_server = sys.argv[2]
    check_wifi_connectivity(hostname)
    # if check_wifi_connectivity(hostname):
    #     #build curl request

    #    	cmd = "iperf -c {}".format(iperf_server)
    #     print("cmd : "+cmd)
    #     output = sp.getoutput(cmd)
    #     print(output)
    #     t.sleep(5)

    #     exit(0)
        
    

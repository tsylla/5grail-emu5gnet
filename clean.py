#!/bin/python3

import subprocess as sp

def get_managed_container_list():
    command_output = sp.getoutput("docker container ls")
    containers = []
    print("Managed Containers list\n")
    for line in command_output.splitlines():
        cols = line.split(" ")
        containers.append(cols[-1])
        print(cols[-1])
    return containers

def get_running_container_list():
    command_output = sp.getoutput("docker ps -a")
    containers = []
    print("Running Containers list \n")
    for line in command_output.splitlines():
        cols = line.split(" ")     
        containers.append(cols[-1])

        # cols = line.split(" ")                
        # if cols[7] != "NAMES":
        #     containers.append(cols[7])
        #     print(cols[7]," - ",cols[13])
        
    return containers    

def stop_running_container(container_list):
    str_start = "mn."
    for container in container_list:
        if str_start in container :
            sp.run(["docker","stop",container])

def remove_managed_container(container_list):
    str_start = "mn."
    for container in container_list:
        if str_start in container :
            sp.run(["docker", "container", "rm", container])

def clean_mn():
    sp.run(["sudo", "mn", "-c"])

if __name__ == "__main__" :
    print("*** Docker container cleaning started.\n")
    
    # print('*** Containers created ...\n')
    # get_managed_container_list() 

   # print("*** Stopping running containers ...\n")
    
    running_ctx = get_running_container_list()
    print("Running container\n")
    #print(running_ctx)
    stop_running_container(running_ctx)

    print('*** Removing containers ..\n')
    remove_managed_container(running_ctx)

    print('*** Cleaning mininet ...')
    clean_mn()

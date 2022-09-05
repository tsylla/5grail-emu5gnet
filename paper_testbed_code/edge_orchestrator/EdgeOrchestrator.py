import os
import logging
import threading
from flask import Flask, send_from_directory
from flask_restful import Api

from emuvim.dcemulator.net import DCNetwork
from emuvim.api.rest.compute import Compute, ComputeResources, ComputeList
import docker
import speedtest
import paper_testbed_code.testbed_utils as tu
import subprocess as sp

class EdgeOrchestrator:

    def __init__(self, edge_datacenters, linked_aps):
        self.edge_datacenters = edge_datacenters
        self.linked_aps = linked_aps

    #place the vnf_properties, the provide vnf is a dict
    def place_service(self, vnf_properties, node):
        dc_name = self.getLeastLoadedDc()
        vnf_name = vnf_properties['vnf_name']
        image = vnf_properties['image']
        volume = vnf_properties['volume']
        cpu_period = vnf_properties['cpu_period']
        cpu_quota = vnf_properties['cpu_quota']
        memory_limit = vnf_properties['mem_limit']

        self.startCompute(dc_name,vnf_name,image,volume,cpu_period,cpu_quota,memory_limit)

    def getLeastLoadedDc(self):
        print("Least load dc")

    def startCompute(self, dc_name, vnf_name, image, volume, cpu_period, cpu_quota, memory_limit):
        command_to_run = "vim-emu compute start -d {} -n {} -i {} -v {} -cpu-p {} -cpu-q {} -mem {}"\
                        .format(dc_name,vnf_name,image,volume,cpu_period,cpu_quota,memory_limit)
        command_output = sp.getoutput(command_to_run)

        return command_output

    def get_dc_cpu_usage(self, vnfs):
        total_cpu_usage = 0
        command_to_run = "docker stats --no-stream "
        for vnf in vnfs:
            command_to_run += 'mn.'+vnf

        command_output = sp.getoutput(command_to_run)

        for line in command_output.splitlines():
            cols = line.split("   ")
            print("Commands results cols ")
            print(cols)
            if not cols[0].__contains__('CONTAINER'):
                cpu_usagestr = cols[2]
                cpu_usagestr = cpu_usagestr.strip()
                posPercent = cpu_usagestr.find("%")
                cpu_usagestr = cpu_usagestr[:posPercent]
                cpu_usage = float(cpu_usagestr)
                total_cpu_usage += cpu_usage

        return total_cpu_usage

    def get_dc_used_memory(self, vnfs):
        used_memory = 0
        command_to_run = "docker stats --no-stream "
        for vnf in vnfs:
            command_to_run += 'mn.'+vnf

        command_output = sp.getoutput(command_to_run)

        for line in command_output.splitlines():
            cols = line.split("   ")
            print("Commands results cols ")
            print(cols)
            if not cols[0].__contains__('CONTAINER'):
                meminbytestr = cols[3]
                meminbytestr = meminbytestr.strip()
                posMiB = meminbytestr.find("MiB")
                meminbytestr = meminbytestr[:posMiB]
                meminbyte = float(meminbytestr)
                used_memory += meminbyte

        return used_memory

    def get_dc_used_bandwidth(self, dc_name, db_file):
        speedtest.get_last_bw_test(dc_name, db_file)

    def get_ctx_id(self, vnf_name):
        client = docker.DockerClient(base_url='unix:///var/run/docker.sock')
        running_ctx = client.containers.list()
        for ctx in running_ctx:
            if ctx.name == vnf_name:
                return ctx.id

    def get_running_vnf_dc(self, dc_name):

        command_to_run = "vim-emu compute list " + dc_name
        command_output = sp.getoutput(command_to_run)
        vnfs = list()
        i = 0

        for line in command_output.splitlines():
            cols = line.split("|")
            if len(cols) > 1:
                if not cols[1].__contains__('Datacenter'):
                    print("Cols number {}".format(len(cols)))
                    print(cols)
                    vnfs.append(cols[2].strip())
            i += 1

        return vnfs


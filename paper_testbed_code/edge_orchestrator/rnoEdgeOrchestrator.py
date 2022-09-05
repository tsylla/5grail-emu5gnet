import logging

import time
from timer import Timer
import math
import docker
import speedtest
import testbed_utils as tu
import subprocess as sp
import os
import testbed_utils as tu
from flask import Flask, abort
from flask_restful import Api, Resource, reqparse, fields, marshal

CORS_HEADER = {'Access-Control-Allow-Origin': '*'}
testbed_dir = os.getenv("TESTBED_DIR")
logging.basicConfig(filename=testbed_dir+"/edge_orchestrator/rno_eo.log",level=logging.DEBUG)

# app = Flask(__name__,static_url_path="")
# api = Api(app)

vnf_fields = {
    'vnf_name': fields.String,
    'node': fields.String,
    'image': fields.String,
    'volume': fields.String,
    'cpu_period': fields.String,
    'cpu_quota': fields.String,
    'memory_limit': fields.String,
    'dc': fields.String,
    'done': fields.Boolean,
    'uri': fields.Url('vnf')
}

trains_file = testbed_dir+"/good_map/osm.rail.trips.xml"
dc_file = testbed_dir + "/dc_names.csv"
access_points_file = testbed_dir + "/ap_names_positions.csv"
volume = "/home/wifi/db:/db"
trains_list = tu.getIdFromXml(trains_file,"trip")
access_points = tu.get_access_point_names(access_points_file)
datacenters = tu.get_dc_names(dc_file)

rno_eo = None
class RNOEdgeResource(Resource):

    global rno_eo
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('vnf_name', type=str, required=True,
                                   help="No VNF name provided", location="json")
        self.reqparse.add_argument('node', type=str, required=True,
                                   help="Node name not provided", location="json")
        self.reqparse.add_argument('image', type=str, required=True,
                                   help="No image provided", location="json")
        self.reqparse.add_argument('volume', type=str, required=True,
                                   help="No volume provided", location="json")
        self.reqparse.add_argument('cpu_period', type=str, required=True,
                                   help="No Cpu Period provided", location="json")
        self.reqparse.add_argument('cpu_quota', type=str, required=True,
                                   help="No Cpu quota provided", location="json")
        self.reqparse.add_argument('mem_limit', type=str, required=True,
                                   help="Memory limit not provided", location="json")
        super(RNOEdgeResource, self).__init__()

    # def put(self):
    #     

    def get(self):
        # rno_eo.check_services_to_place()
        # return {"move":"Service migration process completed"},200, CORS_HEADER
        pass
    
        
    def post(self):
        args = self.reqparse.parse_args()
        vnf = {'vnf_name' : args['vnf_name'],
               'image' : args['image'],
               'volume' : args['volume'],
               'cpu_period' : args['cpu_period'],
               'cpu_quota' : args['cpu_quota'],
               'mem_limit' : args['mem_limit'],
               'node' : args['node'],
               'dc' : '',
               'done' : False
               }

        result = rno_eo.start_compute_from_node(vnf)
        if result['result']:
            vnf['dc'] = result['dc']
            vnf['done'] = True
            return {'vnf' : marshal(vnf, vnf_fields)}, 201, CORS_HEADER
        else:
            abort(404)

class RNOEdgeOrchestrator(object):

    def __init__(self):
        self.running_vnfs = list(dict())
        super(RNOEdgeOrchestrator, self).__init__()

    def get_last_position(self, pos_file):
        pos = list()
        try:
            with open(pos_file, "r") as f:
                contains = f.readlines()
                # lines = contains.splitlines()

                last_line = contains[-1]
                positions = last_line.split(",")
                pos_x = float(positions[0])
                pos_y = float(positions[1])
                pos_z = 0
                pos.append(pos_x)
                pos.append(pos_y)
                pos.append(pos_z)

        except:
            pos = [-1,-1,-1]

        return pos

    def get_distance(self, src, dst):
        """Get the distance between two nodes, read nodes positions from telemetry file
        :param self:
        :param src: source destion
        :param dst: destination node"""
        src_pos_file = testbed_dir+"/position-%s-mn-telemetry.txt"%src
        dst_pos_file = testbed_dir+"/position-%s-mn-telemetry.txt"%dst
        """ Read the last position of both nodes from telemetry position data"""
        pos_src = self.get_last_position(src_pos_file)
        pos_dst = self.get_last_position(dst_pos_file)

        if(pos_dst[0] <= 0.0 or pos_src[0]<=0.0):
            dist = -1
        else:
            x = (float(pos_src[0]) - float(pos_dst[0])) ** 2
            y = (float(pos_src[1]) - float(pos_dst[1])) ** 2
            z = (float(pos_src[2]) - float(pos_dst[2])) ** 2
            dist = math.sqrt(x + y + z)

        return round(dist, 2)

    def get_closest_datacenter(self, node):
        closest_ap = self.get_placement_condition(node)
        if closest_ap is not None :
            dc_name = closest_ap['dc']
        else:
            dc_name = ""

        return dc_name

    def get_placement_condition(self, node):
        distances_to_ap = list(dict())

        for i in range(len(access_points)):
            distance_to_ap = dict()
            ap = access_points[i]
            distance_to_ap['name'] = ap['name']
            distance_to_ap['dc'] = ap['dc']
            distance_to_ap['distance'] = self.get_distance(ap['name'], node)
            if distance_to_ap['distance'] != -1 :
    #            print("Distance of {} to access point {} : {}".format(ap['name'],
    #                node, distance_to_ap['distance']))
                distances_to_ap.append(distance_to_ap)
                #sort the distance list by access points
        if len(distances_to_ap) !=0:
            distances_to_ap = sorted(distances_to_ap,key=lambda i: i['distance'])
        else:
            return None
        #print(f"Most closest AP is : {distances_to_ap[0]['name']}")
        #print(f"Most closest datacenter to {node} is : {distances_to_ap[0]['dc']}")
        return distances_to_ap[0]

    # def first_services_placement(self, volume):
        # for id in trains_list:
        #     node = "t%s"%id
        #     vnf_properties = dict()
        #     vnf_properties['image'] = "vnf:latest"
        #     vnf_properties['volume'] = volume
        #     vnf_properties['cpu_period'] = self.cpu_period
        #     vnf_properties['cpu_quota'] = self.cpu_quota
        #     vnf_properties['mem_limit'] = self.mem_limit
        #     vnf_properties['vnf_name']="vnf-%s"%node
        #     vnf_properties['node'] = node
        #     dc_name = self.get_closest_datacenter(node)
        #     if dc_name != "":
        #         debug = "Train {} service launched on dc {}".format(node,dc_name)
        #         print(debug)
        #         logging.info(debug)
        #         self.start_compute_with_properties(dc_name, vnf_properties)
        #         self.running_vnfs.append(vnf_properties)

    def check_services_to_place(self):
        print("Running VNF : \n")
        t_start = time.perf_counter()
        for vnf in self.running_vnfs :
            node = vnf['node']
            actual_dc = vnf['dc']
            closest_dc = self.get_closest_datacenter(node)
            if closest_dc != "" :
                if actual_dc != closest_dc :
                    #self.place_service(vnf, actual_dc)
                    #TODO check moving result and update counter
                    self.move_compute(closest_dc, vnf)
                    duration = time.perf_counter() - t_start
                    debug= "placement_check started at,{},duration,{}".format(t_start, duration)
                    print(debug)
                    logging.debug(debug)

    #place the vnf_properties, the provide vnf is a dict
    def place_service(self, vnf_properties, actual_dc):
        #check placement conditon
        # check if the current ap is different from the most closest ap
        # then make the placement game with the ap_linked_Eo
        node = vnf_properties['node']

        # play game with eo
        # for simple juste place in dc connected to the apt
        dc_name = self.get_closest_datacenter(node)
        vnf_name = vnf_properties['vnf_name']
        image = vnf_properties['image']
        volume = vnf_properties['volume']
        cpu_period = vnf_properties['cpu_period']
        cpu_quota = vnf_properties['cpu_quota']
        memory_limit = vnf_properties['mem_limit']
        
        #check meme usage/cpu before
        self.start_compute(dc_name,vnf_name,image,volume,cpu_period,cpu_quota,memory_limit)
        
        #check service stats and log
        self.running_vnfs.append(vnf_properties)

    def get_least_loaded_dc(self):
        print("Least load dc")

    def start_compute(self, dc_name, vnf_name, image, volume, cpu_period, cpu_quota, memory_limit):
        command_to_run = "vim-emu compute start -d {} -n {} -i {} -v {} -cpu-p {} -cpu-q {} -mem {}"\
                        .format(dc_name,vnf_name,image,volume,cpu_period,cpu_quota,memory_limit)
        command_output = sp.getoutput(command_to_run)

        return command_output

    def start_compute_with_properties(self, dc_name, vnf_properties):
        vnf_name = vnf_properties['vnf_name']
        if not self.is_vnf_running(vnf_name):
            image = vnf_properties['image']
            volume = vnf_properties['volume']
            cpu_period = vnf_properties['cpu_period']
            cpu_quota = vnf_properties['cpu_quota']
            memory_limit = vnf_properties['mem_limit']
            node = vnf_properties['node']
            
            #associate the vnf with current dc
            vnf_properties['dc'] = dc_name

            command_to_run = "vim-emu compute start -d {} -n {} -i {} -v {} -cpu-p {} -cpu-q {} -mem {}" \
                .format(dc_name, vnf_name, image, volume, cpu_period, cpu_quota, memory_limit)
            t_start = time.perf_counter()
            command_output = sp.getoutput(command_to_run)
            duration = time.perf_counter() - t_start
            debug = "start,{}, service launched on dc {} at,{},duration,{}".format(node, dc_name, t_start,duration)
            print(debug)
            logging.debug(debug)
            #check and log the result
            self.running_vnfs.append(vnf_properties)
            return command_output
        else:
            return f"VNF {vnf_name} is already running and should be may be stop and launch away." \
                   f"Further processing will be implemented soon."

    def start_compute_from_node(self, vnf_properties):
        node = vnf_properties['node']
        dc_name = self.get_closest_datacenter(node)
        if dc_name != "":
            if not self.is_vnf_running(vnf_properties['vnf_name']):
                self.start_compute_with_properties(dc_name, vnf_properties)
                self.running_vnfs.append(vnf_properties)
                return {'result':True,'dc':dc_name}
            else:
                return {'result':False,'dc':None}
        else:
            return {'result':False,'dc':None}

    def is_vnf_running(self, vnf_name):
        result = None
        
        if len(self.running_vnfs) > 0:
            result = next((vnf for vnf in self.running_vnfs if vnf['vnf_name'] == vnf_name), None)
        
        if result is None:
            return False
        else:
            return True

    def update_running_vnfs_dc(self, vnf_name, dc_name):
        vnf = next(item for item in self.running_vnfs if item['vnf_name'] == vnf_name)
        vnf['dc'] = dc_name

    def move_compute(self, next_dc, vnf_properties):
        #TODO move vnf from actual_dc toward next_dc
        actual_dc = vnf_properties['dc']
        name = vnf_properties['vnf_name']
        node = vnf_properties['node']
        cmd = "vim-emu compute move -d {} -dest {} -n {}".format(actual_dc, next_dc, name)
        vnf_properties['dc'] = next_dc    
        t_start = time.perf_counter()      
        sp.getoutput(cmd)
        #update running_vnfs list
        duration = time.perf_counter() - t_start
        self.update_running_vnfs_dc(name, next_dc)
        debug = "move,{}, service move from {} to {},at,{},duration,{}".format(node, actual_dc, next_dc, t_start, duration)
        #debug = "Train {} service moved from dc {} to {}".format(node, actual_dc, next_dc)
        print(debug)
        logging.debug(debug)

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
                pos_percent = cpu_usagestr.find("%")
                cpu_usagestr = cpu_usagestr[:pos_percent]
                cpu_usage = float(cpu_usagestr)
                total_cpu_usage += cpu_usage

        return total_cpu_usage

    def get_dc_used_memory(self):
        used_memory = 0

        command_to_run = "docker stats --no-stream "
        for vnf in self.running_vnfs:
            command_to_run += 'mn.'+vnf['vnf_name'] + ' '

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

# api.add_resource(RNOEdgeOrchestrator, '/vnf/api/start', endpoint='start')
# api.add_resource(RNOEdgeOrchestrator,'/vnf/api/vnf', endpoint='vnf')

# def run_rno_eo():
#     print("Running API server")
#     app.run(debug=False, host="0.0.0.0", port=8899)

# def run_rno_eo_routine():
#     print("Running EO instance")
    
#     #this part will 5 seconds after the program Eo is launched
#     #time.sleep(10)
#    # eo.first_services_placement(volume)

#     """Create a timer for node position sensing and computing moving"""
#     timer = Timer()
#     timer.start()
#     while True:

#         elapsed = timer.get_elapsed()

#         if elapsed >= 10 :
#             print("Checking service to replace")
#             eo.check_services_to_place()

#             #total_memory = eo.

#             # mem_percent = eo.get_dc_used_memory()
#             # cpu_usage = eo.get_dc_cpu_usage()
#             # bandwidth = eo.get_dc_used_bandwidth()
#             # print(f"Used memory : {mem_percent} ")
#             #time.sleep(20)
#             timer.re_start()

# if __name__ == '__main__':

    #eo = RNOEdgeOrchestrator(edge_datacenters=datacenters, trains_list=trains_list,
    #                 access_points = access_points, volume=volume,
    #                          mem_limit='20m', cpu_quota=2000, cpu_period=10000, total_mem='100m')

    # api_thread = Thread(target=run_rno_eo)
    # eo_routine_thread = Thread(target=run_rno_eo_routine)

    # api_thread.start()
    # eo_routine_thread.start()

    # # api_thread.join()
    # # eo_routine_thread.join()

    # exit(0)

import logging
import os
import threading
import time
from gevent.pywsgi import WSGIServer
import testbed_utils as tu
from flask import Flask, jsonify, abort, make_response
from flask_restful import Api, Resource, reqparse, fields, marshal
import rnoEdgeOrchestrator
from rnoEdgeOrchestrator import RNOEdgeResource, RNOEdgeOrchestrator


class RestApiEndpoint(object):

    def __init__(self, listenip, port):
        
        self.ip=listenip
        self.port=port
        self.rno_eo = RNOEdgeOrchestrator()
        rnoEdgeOrchestrator.rno_eo = self.rno_eo
        #self.initRnoEo(rno_eo)

        self.app = Flask(__name__)
        self.api = Api(self.app)

        self.api.add_resource(RNOEdgeResource, '/vnf/api/start', endpoint='start')
        self.api.add_resource(RNOEdgeResource, '/vnf/api/vnf', endpoint='vnf')
#        self.api.add_resource(RNOEdgeResource, '/vnf/api/move', endpoint='move')
        
    def start(self):
        
        self.thread1 = threading.Thread(target=self._start_rno_eo,args=())
        self.thread2 = threading.Thread(target=self._start_routine, args=())
        #self.thread1.daemon = False
        #self.thread2.daemon = False

        self.thread1.start()
        logging.info("Started API endpoint @ http://%s:%d" %
                     (self.ip, self.port))
        self.thread2.start()
        
    def _start_rno_eo(self):        

        self.app.run(self.ip, self.port)

        self.http_server = WSGIServer((self.ip, self.port),
                                      self.app,
                                      # This disables HTTP request logs to not
                                      # mess up the CLI when e.g. the
                                      # auto-updated dashboard is used
                                      log=open("/dev/null", "w")
                                      )
        self.http_server.serve_forever()
    def _start_routine(self):
        """Create a timer for node position sensing and computing moving"""
        timer_d = time.perf_counter()
        
        while True:
            elapsed = time.perf_counter() - timer_d

            if elapsed >= 5 :
                print("Checking service to replace")
                self.rno_eo.check_services_to_place()

                #total_memory = eo.

                # mem_percent = eo.get_dc_used_memory()
                # cpu_usage = eo.get_dc_cpu_usage()
                # bandwidth = eo.get_dc_used_bandwidth()
                # print(f"Used memory : {mem_percent} ")
                #time.sleep(20)
                timer_d = time.perf_counter()

if __name__=="__main__":
    
    restapi = RestApiEndpoint("0.0.0.0",8899)
    restapi.start()
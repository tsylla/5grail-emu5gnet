#!/usr/bin/python3

import sys
import subprocess as sp
import mysql.connector

def test_bandwith(server, port, dbserver):
    command_output = sp.getoutput('iperf3 -c {} -p {} -t 1 -f M'.format(server, port))
    print('{}'.format(command_output))

    result_line = command_output.splitlines()[4 - 1]
    before_bitrate = result_line.find("GBytes") + len("GBytes")
    after_bitrate = result_line.find('MBytes')
    bitrate = float(result_line[before_bitrate:after_bitrate])    
    print('Result line \n{}'.format(result_line))
    print('Bitrate in Mbps : {}'.format(bitrate))
    hostname = sp.getoutput("hostname")
    save_test(dbserver, bitrate, hostname)

def save_test(dbserver, bitrate, hostname):
    conn = None
    try:
        conn = mysql.connector.connect(host=dbserver,user='user', password='user', db='edge_server_management')
        cursor = conn.cursor()

        query = """insert into bandwidth(dc_name, bandwidth) values (%s,%s)"""
        values = (hostname, bitrate)
        print("Insert following values in the table : hostname={} and bitrate={}".format(hostname,bitrate))
        cursor.execute(query, values)
        conn.commit()
        print("Insert query successfully executed.")
        
    except mysql.connector.Error as error:
         print("Failed to insert into MySQL table {}".format(error))
    finally:
        if conn != None :
            if conn.is_connected():
                cursor.close()
                conn.close()
                print("MySQL connection is closed")

if __name__=='__main__':
   
    server = sys.argv[1]
    port = sys.argv[2]
    dbserver = sys.argv[3]
    #print('Arguments passés: 1= {} 2={} 3={}'.format(server,port,dbserver))
    test_bandwith(server,port,dbserver)


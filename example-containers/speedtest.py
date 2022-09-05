#!/usr/bin/python3

import sqlite3
import sys
import subprocess as sp
from sqlite3 import connect


def init_db(filename="/home/wifi/db/testbed_db.db"):
    db_connection = connect(filename)
    db_cursor = db_connection.cursor()

    statement = "CREATE TABLE IF NOT EXISTS bandwidth (idbandwidth INTEGER PRIMARY KEY AUTOINCREMENT, \
        dc_name TEXT, \
        bandwidth REAL);"
    db_cursor.execute(statement)
    statement = "CREATE TABLE IF NOT EXISTS memory (idmem INTEGER PRIMARY KEY AUTOINCREMENT, \
        dc_name TEXT, \
        memory REAL);"
    db_cursor.execute(statement)
    statement = "CREATE TABLE IF NOT EXISTS CPU (idcpu INTEGER PRIMARY KEY AUTOINCREMENT, \
        dc_name TEXT, \
        cpu REAL);"
    db_cursor.execute(statement)

    db_params = dict()
    db_params['cursor'] = db_cursor
    db_params['connect'] = db_connection

    return db_params


def test_bandwidth(server, port, db_file):
    command_output = sp.getoutput('iperf3 -c {} -p {} -t 1 -f M'.format(server, port))
    print('{}'.format(command_output))
    result_line = command_output.splitlines()[4 - 1]
    gbyte_str = "GBytes"
    mbyte_str = "MBytes"
    kbyte_str = "KBytes"
    gbyte_first = result_line.find(gbyte_str, 0, int(len(result_line)/2))
    kbyte_first = result_line.find(kbyte_str,0,int(len(result_line)/2))
    
    if gbyte_first != -1:
        pos1 = result_line.find(gbyte_str)        
        before_bitrate = pos1 + len(gbyte_str)
        after_bitrate = result_line.find(mbyte_str)
    elif kbyte_first != -1:
        pos1 = result_line.find(kbyte_str)
        before_bitrate = pos1 + len(kbyte_str)
        new_str = mbyte_str+"/sec"
        print("Finding %s position"%new_str)
        after_bitrate = result_line.find(mbyte_str+"/sec")
    
    else:
        before_bitrate = result_line.find(mbyte_str)+len(mbyte_str)
        after_bitrate = result_line.find(mbyte_str, before_bitrate + 1)
      
    
    # print("result_lines")
    # print(result_line)
    # if result_line.find("GBytes") != -1:
    #     pos1 = result_line.find("GBytes")        
    #     before_bitrate = pos1 + len("MBytes")
    #     after_bitrate = result_line.find("MBytes")
    # elif result_line.find("MBytes") != -1:
    #     pos1 = result_line.find("MBytes")
    #     before_bitrate = pos1 + result_line.find("MBytes", pos1+(len("MBytes")), len(result_line))
    #     after_bitrate = result_line.find("MBytes")
    # else:
    #     pos1 = result_line.find("KBytes")
    #     before_bitrate = pos1 + len("MBytes")
    #     after_bitrate = result_line.find("MBytes")
    
    bitrate = float(result_line[before_bitrate:after_bitrate])    
    print('Result line \n{}'.format(result_line))
    print('Bitrate in Mbps : {}'.format(bitrate))
    dc_name = sp.getoutput("hostname")
    save_test(bitrate, dc_name,db_file)

# def test_bandwidth2(result_line):
#     print("result_lines")
#     print(result_line)
#     gbyte_str = "GBytes"
#     mbyte_str = "MBytes"
#     kbyte_str = "KBytes"
#     gbyte_first = result_line.find(gbyte_str, 0, int(len(result_line)/2))
#     kbyte_first = result_line.find(kbyte_str,0,int(len(result_line)/2))
    
#     if gbyte_first != -1:
#         pos1 = result_line.find(gbyte_str)        
#         before_bitrate = pos1 + len(gbyte_str)
#         after_bitrate = result_line.find(mbyte_str)
#     elif kbyte_first != -1:
#         pos1 = result_line.find(kbyte_str)
#         before_bitrate = pos1 + len(kbyte_str)
#         new_str = mbyte_str+"/sec"
#         print("Finding %s position"%new_str)
#         after_bitrate = result_line.find(mbyte_str+"/sec")
    
#     else:
#         before_bitrate = result_line.find(mbyte_str)+len(mbyte_str)
#         after_bitrate = result_line.find(mbyte_str, before_bitrate + 1)
      

#     #"[  4]   0.00-1.01   sec  1.88 KBytes  1.86 MBytes/sec    0    178 KBytes   "
#     print(f"Before bitrate {before_bitrate}")
#     print(f"After bitrate {after_bitrate}")

#     bitrate = result_line[before_bitrate:after_bitrate]
#     bitrate = float(result_line[before_bitrate:after_bitrate])    
#     print('Extracted from Result line \n{}'.format(bitrate))
#     #print('Bitrate in Mbps : {}'.format(bitrate))

def save_test(bitrate, dc_name, db_file):

    db_params = init_db(filename=db_file)
    db_cursor = db_params['cursor']
    db_connect = db_params['connect']   

    query = "INSERT INTO bandwidth(dc_name, bandwidth) values (:dc_name,:bandwidth)"
    data = {
        'dc_name': dc_name,
        'bandwidth': bitrate}   
    print("Insert following values in the table : dc_name={} and bitrate={}".format(dc_name,bitrate))
    db_cursor.execute(query, data)
    print("Insert query successfully executed.")
    db_connect.commit()


def get_last_bw_test(dc_name):
    db_params = init_db()
    db_cursor = db_params['cursor']
    db = db_params['connect']

    statement = "SELECT * FROM bandwidth WHERE dc_name=:dc_name ORDER BY idbandwidth ASC;"
    data = {'dc_name':dc_name}

    rows = db_cursor.execute(statement, data)
    last_row = rows.fetchone()

    bitrate = 0.0
    bitrate = float(last_row[2])
    
    db_cursor.close()
    db.close()
    return bitrate  


def get_all_bw_test():
    db_params = init_db()
    db_cursor = db_params['cursor']
    db = db_params['connect']

    statement = "SELECT * FROM bandwidth ORDER BY idbandwidth ASC;"
    rows = db_cursor.execute(statement)
    all_rows = rows.fetchall()

    print(all_rows)  # sqlite3.Cursor
    # for row in all_rows:
    #     print(type(row))  # tuple
    #     print(row)
    db_cursor.close()
    db.close()

if __name__=='__main__':
   
    server = sys.argv[1]
    port = sys.argv[2]
    db_file = sys.argv[3]
    #print('Arguments passés: 1= {} 2={} 3={}'.format(server,port,dbserver))
    test_bandwidth(server,port,db_file)

    # test = "[  4]   0.00-1.01   sec  1.88 MBytes  1.86 MBytes/sec    0    178 KBytes   "
    # test_bandwidth2(test)
    # dc_name = "wifi-virtualbox"
    # bitrate = get_last_bw_test(dc_name)

    # print("Last dc : {} speedtest : {} ".format(dc_name, bitrate))

    # print("All test : \n")
    # get_all_bw_test()
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


def test_bandwidth(server, port):
    command_output = sp.getoutput('iperf3 -c {} -p {} -t 1 -f M'.format(server, port))
    print('{}'.format(command_output))

    result_line = command_output.splitlines()[4 - 1]
    before_bitrate = result_line.find("GBytes") + len("GBytes")
    after_bitrate = result_line.find('MBytes')
    bitrate = float(result_line[before_bitrate:after_bitrate])    
    print('Result line \n{}'.format(result_line))
    print('Bitrate in Mbps : {}'.format(bitrate))
    dc_name = sp.getoutput("hostname")
    save_test(bitrate, dc_name)

def save_test(bitrate, dc_name):

    db_params = init_db()
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


def get_last_bw_test(dc_name, db_file):
    db_params = init_db(filename=db_file)
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
    
    #print('Arguments passés: 1= {} 2={} 3={}'.format(server,port,dbserver))
    test_bandwidth(server,port)
    # dc_name = "wifi-virtualbox"
    # bitrate = get_last_bw_test(dc_name)

    # print("Last dc : {} speedtest : {} ".format(dc_name, bitrate))

    # print("All test : \n")
    # get_all_bw_test()
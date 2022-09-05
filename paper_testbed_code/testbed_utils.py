
from xml.dom import minidom
import csv


def getIdFromXml(file, param):
    xmldoc = minidom.parse(file)

    trip = xmldoc.getElementsByTagName(param)
    ids = list()
    #print("Trips found : ")
    #print(trip)

    for element in trip :
        id = element.getAttribute("id")
        #print("Id read : {}\n".format(id))
        ids.append(id)
    return ids

def setIdInXml(file, param, start=1):

    xmldoc = minidom.parse(file)
    trip = xmldoc.getElementsByTagName(param)

    i = start
    for element in trip:
        element.attributes["id"].value = str(i)
        i+=1
    
    with open(file,"w") as f :
        f.write(xmldoc.toxml())

def get_access_point_names(file):

    aps = list(dict())
    with open(file, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)
        lc = 0
        i=0
        for row in csv_reader :
            ap = dict()
            print("row : {}".format(row))
            if lc >= 1 :
                ap['id'] = row[0]
                ap['x'] = row[1]
                ap['y'] = row[2]
                ap['name'] = row[3]
                ap['channel'] = row[4]
                ap['eo'] = row[5]
                ap['dc'] = row[6]
                print("Adding AP : {}".format(ap))
                aps.append(ap)
                i+=1
            lc += 1
            
    return aps

def get_eo_connected_access_points(access_points, eo_name):
    eo_aps = [ap for ap in access_points if ap['eo']==eo_name]

def get_eo_dc_names(dcs, eo_name):
    eo_dcs = [dc for dc in dcs if dc['eo']==eo_name]

    return eo_dcs


def get_dc_names(file):
    dcs = list(dict)

    with open(file, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)
        lc = 0
        i=0
        for row in csv_reader:
            dc = dict()
            if lc>=1:
                dc['dc_name'] = row[0]
                dc['eo'] = row[1]
                dcs.append(dc)
                i+=1
            lc+=1
    return dcs
if __name__== "__main__":
    
    #file = "good_map/osm.passenger.trips.xml"
    file = "good_map/berlin.rou.xml"
    # trains_ids = getIdFromXml(file)
    # print("Trains ids :")
    # print(trains_ids)
    setIdInXml(file,"vehicle")
    print("Trains ids after modification")
    
    trains_ids = getIdFromXml(file,"vehicle")
    print(trains_ids)
    #file = "ap_names_positions.csv"

    #urban_trains = getIdFromXml(file)
    #aps = get_access_point_names(file)

    #print("Access points are : \n")
    #print(aps)
    # print("Id extracted from {} are : \n".format(file))
    # print(urban_trains)
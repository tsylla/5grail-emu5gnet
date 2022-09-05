def get_last_position(pos_file):
    pos = list()
    with open(pos_file, "r") as f:
        contains = f.readlines()
        #lines = contains.splitlines()

        last_line = contains[-1]

        positions = last_line.split(",")
        pos_x = float(positions[0])
        pos_y = float(positions[1])
        pos_z = 0
        pos.append(pos_x)
        pos.append(pos_y)
        pos.append(pos_z)
    return pos

if __name__ == "__main__":
    # file = "/home/wifi/mininet-wifi/examples/position-car9-mn-telemetry.txt"
    # pos = get_last_position(file)
    #
    # print("Last position is : ")
    #
    # print(pos)

    distances = list(dict())
    d = dict()
    d['name'] = 'a'
    d['distance'] = 20.5
    distances.append(d)
    d = dict()
    d['name'] = 'b'
    d['distance'] = 1
    distances.append(d)
    d = dict()
    d['name'] = 'c'
    d['distance'] = -1
    distances.append(d)
    d = dict()
    d['name'] = 'd'
    d['distance'] = 0
    distances.append(d)
    d = dict()
    d['name'] = 'e'
    d['distance'] = 40.5
    distances.append(d)
    print("distances before sorting")
    print(distances)
    new_distances = sorted(distances, key=lambda i:i['distance'])

    print("New distances after sorting : ")
    print(new_distances)
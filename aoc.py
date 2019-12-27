# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 13:33:49 2019

@author: adam.trexler
"""

import math
import networkx as nx


def fuel_counter_upper(mass):
    """
    Day 1: AOC: Fuel Counter-Upper
    """
    if mass <= 0:
        fuel = 0
    else:
        fuel = math.floor(mass / 3) - 2
    return fuel

def find_total_fuel(payload):
    c = 0
    new_fuel = payload
    total_fuel = 0
    while c <= 50:
        new_fuel = fuel_counter_upper(new_fuel)
        
        if new_fuel <= 0:
            break
        else:
            total_fuel += new_fuel 
            c += 1
    return total_fuel

def intcode_reader(l,pos):
    if l[pos] == 1:
        output = l[l[pos+1]] + l[l[pos+2]]
    elif l[pos] == 2:
        output = l[l[pos+1]] * l[l[pos+2]]
    l[l[pos+3]] = output
    return l

def intcode_driver(data):
    for ix in range(0,len(data),4):
        if data[ix] == 99:
            break
        data = intcode_reader(data,ix)
    return data

def wire_grid_path(wirelist,step_mode = False):
    origin = (0,0)
    wirepath = [origin]

    for step in wirelist:
        direction = step[0]
        distance = int(step[1:])
        if direction == "R":
            pts = [(wirepath[-1][0]+(1+i),wirepath[-1][1]) for i in range(distance)]
        elif direction == "L":
            pts = [(wirepath[-1][0]-(1+i),wirepath[-1][1]) for i in range(distance)]
        elif direction == "U":
            pts = [(wirepath[-1][0],wirepath[-1][1]+(1+i)) for i in range(distance)]
        elif direction == "D":
            pts = [(wirepath[-1][0],wirepath[-1][1]-(1+i)) for i in range(distance)]
        else:
            print("invalid direction encountered.")
        [wirepath.append(p) for p in pts]
    if step_mode == True:
        ret = {}
        for i,k in enumerate(wirepath):
            if k not in ret.keys():
                ret[k] = i
    else:
        ret = wirepath
    return ret

def get_wire_intersection(wire1,wire2,int_mode=False):
    """
    return manhattan distance of closest intersection to origin
    """
    if int_mode == False:
        foo = list(set(wire_grid_path(wire1)).intersection(wire_grid_path(wire2)))
        tmp = list(map(lambda x: sum([abs(f) for f in x]),foo))
        ret = sorted(tmp)[1]
    else:
        w1 = wire_grid_path(wire1,step_mode=True)
        w2 = wire_grid_path(wire2,step_mode=True)
        foo = list(set(list(w1.keys())).intersection(list(w2.keys())))
        tmp = list(map(lambda x: sum([abs(f) for f in x]),foo))
        derp = []
        for k in foo:
            derp.append(w1[k]+w2[k])
        ret = sorted(derp)[1]

    return ret

def read_wire_list(raw_wirelist):
    return raw_wirelist.split(",")

def pw_valid(pw):
    pw = str(pw)
    if len(pw) != 6:
        return False
    badval = 0
    dupe = 0
    for i,num in enumerate(pw):
        if i!=len(pw)-1:
            if num==pw[i+1]:
                dupe = 1
    for k,num2 in enumerate(pw):
        if k != len(pw)-1:
            if pw[k+1]<num2:
                badval = 1
    
    if dupe == 1 and badval == 0:
        return True
    else:
        return False

def pw_valid_pt2(pw):
    tmp = {}
    for p in str(pw):
        if p not in tmp.keys():
            tmp[p] = 1
        else:
            tmp[p] += 1
    return True if 2 in tmp.values() else False

""" day 5 """
def intcode_mk2(data,prog_input):
    ix = 0 
    def helper(data,howmany,ix,modes):
        pos = {}
        for x in range(howmany):
            x += 1
            pos[x] = int(data[int(data[ix+x])]) if modes[x] == '0' else int(data[ix+x])
        return pos
        
    while ix < len(data):
        opcode = str(data[ix]).zfill(5) 
        instruction = opcode[-2:] #get opcode last two digits
        modes = {1:opcode[-3],
                 2:opcode[-4],
                 3:opcode[-5]}
        
        if instruction == "01":
            pos = helper(data,2,ix,modes)
            output = int(pos[1]) + int(pos[2])
            data[int(data[ix+3])] = output
            step = 4
        elif instruction == "02":
            pos = helper(data,2,ix,modes)
            output = int(pos[1]) * int(pos[2])
            data[int(data[ix+3])] = output
            step = 4
        elif instruction == "03":
            # input instruction
            pos = helper(data,1,ix,modes)
            data[int(data[ix+1])] = prog_input
            step = 2
        elif instruction == "04":
            # output instruction
            pos = helper(data,1,ix,modes)
            print(ix,":",pos[1])
            ret = pos[1]
            step = 2
        elif instruction == "05":
            #jump-if-true
            pos = helper(data,2,ix,modes)
            if pos[1] != 0:
                ix = pos[2]
                step = 0
            else:
                step = 3
        elif instruction == "06":
            #jump-if-false
            pos = helper(data,2,ix,modes)
            if pos[1] == 0:
                ix = pos[2]
                step = 0
            else:
                step = 3
        elif instruction == "07":
            # less than
            pos = helper(data,3,ix,modes)
            if pos[1] < pos[2]:
                data[int(data[ix+3])] = 1
            else:
                data[int(data[ix+3])] = 0
            step = 4
        elif instruction == "08":
            # equals
            pos = helper(data,3,ix,modes)
            if pos[1] == pos[2]:
                data[int(data[ix+3])] = 1 #set to data[ix+3], since no option for immediate mode.
            else:
                data[int(data[ix+3])] = 0
            step = 4
        elif instruction == "99":
            print("end found")
            break
        else:
            print("invalid opcode {x}".format(x=instruction))
        ix += step
    return ret


""" day 6 """
def create_edge_list(edges):
    """
    convert input orbit data to list of tuples specifying 
    nodes separated by an edge
    """
    ret = [tuple(e.split(")")) for e in edges]
    return ret

def calc_orbital_checksum(orbits):
    """
    calculate the orbital checksum from orbits, an nx 
    undirected graph object. 
    orbitl checksum is the total number of direct and indirect
    orbits in the data.
    
    """
    return sum([nx.shortest_path_length(orbits,node,'COM') if node != 'COM' else 0 for node in orbits.nodes])

def create_orbit_graph(edges):
    """
    create orbits graph from input data of edges.
    """
    
    udg = nx.Graph()
    udg.add_edges_from(edges)
    return udg      

def orbital_transfer_num(orbits,n1,n2):
    """
    get orbital transfers to put object in orbit around n1 and n2
    into orbit around n2.
    """     
    return nx.shortest_path_length(orbits,n1,n2) - 2
    
        
    
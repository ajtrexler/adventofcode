# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 13:33:49 2019

@author: adam.trexler
"""

import math

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
    
        
    
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 13:55:28 2019

@author: adam.trexler
"""
import aoc
import copy

"""
Day 1:
What is the sum of the fuel requirements for all of the modules on your spacecraft?

"""

total = 0

with open("./data/day1.txt","r") as f:
    for row in f.readlines():
        total += aoc.fuel_counter_upper(int(row))    
        


"""
Day 1b:
What is the total sum of the payload + fuel required?
"""

total = 0

with open("./data/day1.txt","r") as f:
    for row in f.readlines():
        total += aoc.find_total_fuel(int(row))    
        
"""
Day 2a:
    opcode.
"""

with open("./data/day2.txt","r") as f:
    data = f.read()
data = [int(i) for i in data.split(",")]
data[1] = 12
data[2] = 2
foo = aoc.intcode_driver(data)
foo[0]

"""
Day 2b:
    brute force find the noun and verb
"""

with open("./data/day2.txt","r") as f:
    data = f.read()
data = [int(i) for i in data.split(",")]

mydict = {}
result = 0
for n in range(1,100):
    print(n)
    for v in range(1,100):
        foo = copy.deepcopy(data)
        foo[1]=n
        foo[2]=v
        tmp = aoc.intcode_driver(foo)
        mydict[(n,v)] = tmp[0]
        if tmp[0] == 19690720:
            print(n,v)
            result = (n,v)
        del(foo,tmp)

"""
Day 3a: get closest wire intersection to central port

"""

with open("./data/day3.txt","r") as f:
    data = f.read()
wire1 = data.split("\n")[0]
wire2 = data.split("\n")[1]

aoc.get_wire_intersection(aoc.read_wire_list(wire1),aoc.read_wire_list(wire2))

"""
Day 3b:
    get closest by steps on wirepath, not manhattan distance.


"""

with open("./data/day3.txt","r") as f:
    data = f.read()
wire1 = data.split("\n")[0]
wire2 = data.split("\n")[1]

aoc.get_wire_intersection(aoc.read_wire_list(wire1),aoc.read_wire_list(wire2),int_mode=True)


"""
day 4a:
    iterate over all numbers in range, identify which ones have consecutive digits, 
    then further identify which ones never decrease
    
"""

foo = list(map(lambda x: aoc.pw_valid(x),list(range(359282,8204010))))
sum(foo)
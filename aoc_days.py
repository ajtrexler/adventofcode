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


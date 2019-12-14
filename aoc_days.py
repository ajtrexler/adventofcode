# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 13:55:28 2019

@author: adam.trexler
"""
import aoc

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
Day 2:
    opcode.
"""

with open("./data/day2.txt","r") as f:
    data = f.read()
data = [int(i) for i in data.split(",")]
data[1] = 12
data[2] = 2
foo = aoc.intcode_driver(data)
foo[0]

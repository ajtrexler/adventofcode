# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 21:07:38 2019
day 7: advent of code 2019
@author: adam.trexler
"""
import aoc 
import itertools

with open("./data/day7.txt", "r") as f:
    data = f.read()         
    data = data.split(",")

program = data

value = []
for i in itertools.permutations(range(5),5):
    phase_seq = list(i)
    value.append(aoc.amplifier_controller(program,phase_seq))
print("part A:",max(value))    

prog3 = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,
27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]
phase_seq = [9,8,7,6,5]

aoc.amplifier_controller(prog3,phase_seq,controller_mode = "feedback")

prog4 = [3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,
-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,
53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10]
phase_seq = [9,7,8,5,6]
aoc.amplifier_controller(prog4,phase_seq,controller_mode = "feedback")

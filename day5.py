# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 20:15:44 2019

@author: adam.trexler
"""
import aoc

def main():
    with open("./data/day5.txt", "r") as f:
        data = f.read()         
        data = data.split(",")
    print("part A: ",aoc.intcode_mk2(data,prog_input = 1))
    
    with open("./data/day5.txt", "r") as f:
        data = f.read()         
        data = data.split(",")
        
    print("part B: ",aoc.intcode_mk2(data,prog_input = 5))
    
       
if __name__ == '__main__':
    main()
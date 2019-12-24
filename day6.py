# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 09:39:33 2019

@author: adam.trexler
"""
import aoc

def main():
    with open("./data/day6.txt", "r") as f:
        data = f.read()         
        data = data.split("\n")
    
    data = data[:-1] # remove '' entry from list.
    edges = aoc.create_edge_list(data)
    orbits = aoc.create_orbit_graph(edges)
    checksum = aoc.calc_orbital_checksum(orbits)
    print("Oribital checksum (part A) is: ",checksum)
    
    transfers = aoc.orbital_transfer_num(orbits,"YOU","SAN")
    print("number of transfers (part B) is: ",transfers)
    

if __name__ == '__main__':
    main()
    
    
    
    





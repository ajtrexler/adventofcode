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

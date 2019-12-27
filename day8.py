# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 22:06:50 2019
day 8: advent of code
@author: adam.trexler
"""

import numpy as np
from collections import Counter

with open("./data/day8.txt", "r") as f:
    data = f.read()         
    data = data.replace("\n","")
    data = [int(d) for d in data]

layers = []
zero_digits = []
for ix in range(0,len(data),150):
    tmp = data[ix:ix+150]
    layers.append(tmp)
    zero_digits.append(sum([i==0 for i in tmp]))

minzero_layer = layers[np.argmin(zero_digits)]
foo = Counter(minzero_layer)

answer = foo[1]*foo[2]
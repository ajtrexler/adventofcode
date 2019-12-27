# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 22:06:50 2019
day 8: advent of code
@author: adam.trexler
"""

import numpy as np
from collections import Counter
import matplotlib.pyplot as plt

def main():
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
    print("oart A:",answer)
    
    # more complex with numpy array
    # it is not clear why this did not work.  
    # data = np.array(data).reshape(6,25,100)
    # decoded = np.array([(data[i,k,:][data[i,k,:] != 2])[0] for k in range(25) for i in range(6)]).reshape(6,25)
    
    vals = []    
    for ix in range(150):
        s = [data[i+ix] for i in range(0,len(data),150)]
        foo = (np.array(s)[[ss!=2 for ss in s]])[0]
        vals.append(foo)

    decode2 = np.array(vals).reshape(6,25)
    np.set_printoptions(formatter={'all':lambda x: ' ' if x==0 else 'x'})
    print("############\n")
    print(decode2)
    #plt.imshow(decode2)

if __name__ == '__main__':
    main()



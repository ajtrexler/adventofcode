# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 07:59:02 2019

@author: adam.trexler
"""

import aoc
def main():
    foo = list(map(lambda x: aoc.pw_valid(x),list(range(359282,820401))))
    print(sum(foo))
    
    woo = list(map(lambda x: 1 if aoc.pw_valid(x) and aoc.pw_valid_pt2(x)  else 0,list(range(359282,820401))))
    print(sum(woo))
    
        

if __name__ == '__main__':
    main()
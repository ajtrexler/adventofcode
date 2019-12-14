# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 13:44:25 2019
unittests for advent of code module

@author: adam.trexler
"""

import unittest
import aoc

class testAOC(unittest.TestCase):
    
    def test_fuel_counter(self):
        self.assertEqual(2,aoc.fuel_counter_upper(12))
        self.assertEqual(2,aoc.fuel_counter_upper(14))
        self.assertEqual(654,aoc.fuel_counter_upper(1969))
        self.assertEqual(33583,aoc.fuel_counter_upper(100756))
        self.assertEqual(0,aoc.fuel_counter_upper(0))
        
    def test_total_fueler(self):
        self.assertEqual(50346,aoc.find_total_fuel(100756))
        self.assertEqual(966,aoc.find_total_fuel(1969))
    
    def test_opcoder(self):
        test = [1,9,10,3,2,3,11,0,99,30,40,50]

        self.assertEqual([3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50],
                         aoc.intcode_driver(test))
        
if __name__ == '__main__':
    unittest.main()

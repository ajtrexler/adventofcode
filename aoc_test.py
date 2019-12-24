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
        
#    def test_wirepath(self):
#        testwire1 = "R8,U5,L5,D3"
#        testwire2 = "U7,R6,D4,L4"
#        testwire3 = "R75,D30,R83,U83,L12,D49,R71,U7,L72"
#        testwire4 = "U62,R66,U55,R34,D71,R55,D58,R83"
#        testwire5 = "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51"
#        testwire6 = "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"
#        
#        self.assertEqual(6,aoc.get_wire_intersection(aoc.read_wire_list(testwire1),
#                                  aoc.read_wire_list(testwire2)))
#        self.assertEqual(159,aoc.get_wire_intersection(aoc.read_wire_list(testwire3),
#                                  aoc.read_wire_list(testwire4),int_mode=True))
#        self.assertEqual(135,aoc.get_wire_intersection(aoc.read_wire_list(testwire5),
#                                  aoc.read_wire_list(testwire6)))     
#        
    def test_pw(self):
        self.assertEqual(False,aoc.pw_valid(1111))
        self.assertEqual(False,aoc.pw_valid(111154))
        self.assertEqual(False,aoc.pw_valid(123456))
        self.assertEqual(True,aoc.pw_valid(111122))
        self.assertEqual(True,aoc.pw_valid(112233))
        self.assertEqual(True,aoc.pw_valid(123345))
        self.assertEqual(True,aoc.pw_valid(112344))
        
    def test_orbits(self):
        test_nodes = ["COM)B","B)C","C)D","D)E","E)F","B)G","G)H","D)I","E)J","J)K","K)L"]
            


        
        
        
if __name__ == '__main__':
    unittest.main()

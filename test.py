#!/usr/bin/env python3
import unittest
from minidf import *
import shutil
import argparse

class testMiniDf(unittest.TestCase):
    def test_diskspace_valid_path(self):
        print("Valid test case")
        path = "/Users/skovili/"
        total_a, free_a, used_a = calc(path)
        print ("Result: ")
        print (total_a, free_a, used_a)
        self.assertEqual(total_a, '499963174912')
        self.assertEqual(free_a, '408553115648')
        self.assertEqual(used_a, '70584012800')

if __name__ == '__main__':
    unittest.main()
    
    
        

    

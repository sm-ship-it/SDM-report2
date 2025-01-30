#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):

        def test_valid(self):
                self.assertEqual (2, calc(1,2))
                self.assertEqual (99, calc(1,99))

        def test_invalid_c (self):
                self.assertEqual (-1, calc('N',5))
                self.assertEqual (-1, calc(5,'T'))
                self.assertEqual (-1, calc('N','T'))

        def test_invalid_f (self):
                self.assertEqual (-1, calc(0.4,8))
                self.assertEqual (-1, calc(1,8.8))
                self.assertEqual (-1, calc(0.4,8.8))
        
        def test_invalid_out (self):
                self.assertEqual (-1, calc(-8,20))
                self.assertEqual (-1, calc(20,8))
                self.assertEqual (-1, calc(8,2008))
                self.assertEqual (-1, calc(-8,-20))
                self.assertEqual (-1, calc(1000,2008))
                self.assertEqual (-1, calc(-8,2008))

        def test_boundary (self):
                self.assertEqual (-1, calc(0,8))
                self.assertEqual (8, calc(1,8))
                self.assertEqual (-1, calc(8,8))
                self.assertEqual (7992, calc(8,999))
                self.assertEqual (-1, calc(8,1000))
                self.assertEqual (997002, calc(998,999))


#!/usr/bin/env python3
'''
Lesson03 - Assignment 01 - Unit test cases for Recursive Factorial Implementation
Author: Sireesha Sankuratripati
'''
import unittest

from factorial import *

class TestFactorial(unittest.TestCase):

	def test_input_zero(self):
		self.assertEqual(factorial(0),1)

	def test_input_one(self):
		self.assertEqual(factorial(1),1)
	
	def test_input_negative_fail(self):
		with self.assertRaises(ValueError):
			output = factorial(-10)

	def test_input_seven(self):
		self.assertEqual(factorial(7),5040)

	def test_input_ten(self):
		self.assertEqual(factorial(10),3628800)
		
	def test_input_hundred(self):
		self.assertEqual(factorial(100),93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000)

if __name__ =='__main__':
	unittest.main()
#!/usr/bin/env python3
'''
Lesson03 - Activity 01 - Locke Unit tests class
Author: Sireesha Sankuratripati
'''

import unittest
import io
import sys

from locke import Locke

class TestLocke(unittest.TestCase):
	message = "Stoppng the Pumps. \nOpening the doors.\nClosing the doors. \nRestarting the pumps."

	def test_move_boats_less_than_capacity(self):
		number_boats = 8
		capacity = 10
		locke = Locke(capacity)
		expected_output = "*********  Moved 8 boats through the Locke successfully  *********"
		capturedOutput = io.StringIO()  
		sys.stdout = capturedOutput
		locke.move_boats_through(number_boats)
		sys.stdout = sys.__stdout__ 
		self.assertEqual(capturedOutput.getvalue().strip(), expected_output.strip())

	def test_move_boats_greater_than_capacity_fail(self):
		number_boats = 12
		capacity = 10
		locke = Locke(capacity)		
		with self.assertRaises(ValueError):
			locke.move_boats_through(number_boats)

if __name__ == '__main__':
	unittest.main()
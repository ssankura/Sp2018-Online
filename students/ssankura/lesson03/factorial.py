#!/usr/bin/env python3
'''
Lesson03 - Assignment 01 - Recursive Factorial Implementation
Author: Sireesha Sankuratripati
'''

def factorial(n):
	'''
	Recursive implementation of Factorial
	'''
	if n<0: raise ValueError("Invalid Input for Factorial {}".format(n))
	if n==0: return 1
	if n>=1: return (n * factorial(n-1))

if __name__ == '__main__':
	print ("Factorial of {} is {}".format(0,factorial(0)))
	print ("Factorial of {} is {}".format(1,factorial(1)))
	print ("Factorial of {} is {}".format(5,factorial(5)))
	print ("Factorial of {} is {}".format(10,factorial(10)))
	print ("Factorial of {} is {}".format(100,factorial(100)))

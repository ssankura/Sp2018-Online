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
	if n==1: return 1
	if n>=2: return (n * factorial(n-1))

if __name__ == '__main__':
	print(factorial(10))



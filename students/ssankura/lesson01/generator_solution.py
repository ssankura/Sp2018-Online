
'''
Lesson01: Assignment 1 - Generators
Author: Sireesha Sankuratripati
'''

def intsum(start_val = 0):
	''' Sum of Integers - keep adding the next integer
	0 + 1 + 2 + 3 + 4 + 5 + …
	so the sequence is:
	0, 1, 3, 6, 10, 15 …..
	'''
	new = start_val
	prev = start_val
	sum_nums = start_val
	while True:
		yield sum_nums
		new = prev + 1
		sum_nums += new
		prev = new

def intsum2(start_val = 0):
	''' Sum of Integers generator- keep adding the next integer
	0 + 1 + 2 + 3 + 4 + 5 + …
	so the sequence is:
	0, 1, 3, 6, 10, 15 …..
	'''
	new = start_val
	prev = start_val
	sum_nums = start_val
	while True:
		yield sum_nums
		new = prev + 1
		sum_nums = sum_nums + new
		prev = new

def doubler(start_val = 1):
	'''Doubler generator
	Each value is double the previous value:
	1, 2, 4, 8, 16, 32,
	'''
	new = start_val
	prev = start_val
	while True:
		yield new
		new = prev * 2
		prev = new

def fib(start_val = 0):
	'''Fibonacci sequence of numbers generator
	The Fibonacci sequence as a generator:
	f(n) = f(n-1) + f(n-2)
	1, 1, 2, 3, 5, 8, 13, 21, 34…
	'''
	prev_fib = start_val
	fib = start_val +1
	while True:
		temp_val = fib
		yield fib
		fib = fib + prev_fib
		prev_fib = temp_val


import math
def prime():
	'''Prime Numbers generator'''
	element = 1
	while True:
		if is_prime(element):
			yield element 
		element = element + 1

def is_prime(number):
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for current in range(3, int(math.sqrt(number) + 1), 2):
            if number % current == 0: 
                return False
        return True
    return False
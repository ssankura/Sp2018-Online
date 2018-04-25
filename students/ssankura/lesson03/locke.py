#!/usr/bin/env python3
'''
Lesson03 - Activity 01 - Locke Implementation
Author: Sireesha Sankuratripati
'''
class Locke(object):
	def __init__(self, capacity_boats):
		self.capacity_boats = capacity_boats

	def __enter__(self):
		print ("********* Entering the Locke  *********")
		self.printUserMessage()
		return self

	def __exit__(self, type, value, tb):
		print ("********* Exiting the Locke  *********")
		self.printUserMessage()

	def move_boats_through(self, num_boats):
		if num_boats > self.capacity_boats:
			raise ValueError("Capacity Error with number of boats -{}. Maximum number of Boats allowed is {}. ".format(num_boats, self.capacity_boats))
		print ("*********  Moved {} boats through the Locke successfully  *********".format(num_boats))

	def printUserMessage(self):
		message = "Stoppng the Pumps. \nOpening the doors.\nClosing the doors. \nRestarting the pumps."
		print (message)


if __name__ == "__main__":
	number_boats = 8
	capacity_boats = 5
	capacity_boats_large = 10
	small_locke = Locke(capacity_boats)
	large_locke = Locke(capacity_boats_large)

	with  large_locke as obj_locke:
		obj_locke.move_boats_through(number_boats)

	with small_locke as obj_locke:
		try:
			obj_locke.move_boats_through(number_boats)
		except ValueError as e:
			print ("********* Exception occured in move_boats_through for number_of_boats - {} Exception: {} *********".format(number_boats,e))

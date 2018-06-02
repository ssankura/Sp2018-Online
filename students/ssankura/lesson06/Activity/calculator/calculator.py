"""
Lesson06 - Activity 1
Author: Sireesha Sankuratripati
Implementation of Calculator
"""


from .exceptions import InsufficientOperands


class Calculator(object):
    """ Implementation of the Calculator Class """

    def __init__(self, adder, subtracter, multiplier, divider):
        """Constructor for Calculator"""

        self.adder = adder
        self.subtracter = subtracter
        self.multiplier = multiplier
        self.divider = divider

        self.stack = []

    def enter_number(self, number):
        """ enter the number on which an operation needs to be performed
            the number will get inserted into the stack"""

        self.stack.insert(0, number)

    def _do_calc(self, operator):
        """ Perform the calculation based on the mathemarical operation
            specified in the operator argument"""

        try:
            result = operator.calc(self.stack[1], self.stack[0])
        except IndexError:
            raise InsufficientOperands

        self.stack = [result]
        return result

    def add(self):
        """ Add method which calls the calc method
            on the adder object """

        return self._do_calc(self.adder)

    def subtract(self):
        """ Subtract method which calls the calc method
            on the subtracter object """

        return self._do_calc(self.subtracter)

    def multiply(self):
        """ Multiply method which calls the calc method
            on the multiplier object """

        return self._do_calc(self.multiplier)

    def divide(self):
        """ Divide method which calls the calc method
            on the divider object """

        return self._do_calc(self.divider)

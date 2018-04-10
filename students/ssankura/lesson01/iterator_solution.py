#!/usr/bin/env python

"""
Lesson01 - Assignment1 - Iterator code
Author: Sireesha Sankuratratipati
"""


class IterateMe_2(object):
    """
    New Iterator class which mimics the functionality of range
    allows to set start, stop and step of an iteration
    """

    def __init__(self, start, stop, step = 1):
        #self.current = -1
        self.current = start - step #current = start index -1  
        self.start = self.current
        self.stop = stop
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        self.current += self.step
        if self.current < self.stop:
            return self.current
        else:
            raise StopIteration


if __name__ == "__main__":

    print("Testing the iterator")
    it = IterateMe_2(2,20,2)
    for i in it:
        if i > 10: break
        print(i)

    print ("print using iterator after break ")
    for i in it:
        print(i)

    print ('Print test using range')
    range1 = range(2,20,2)
    for i in range1:
        if i > 10: break
        print(i)

    print ("print using range after break ")
    for i in range1:
        print (i)

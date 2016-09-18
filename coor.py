#!/usr/bin/env python

import nose as n

"""
This module will return a list of n + 1 equally spaced coordinates in a given range
"""


def coor(n,a,b):
    """
    Calculates a list of coordinates using a for loop
    """
    coordinates = []
    length = (b-a)/float(n+1)
    for i in range(n+1):
        coordinates.append(a + length * (i + 1))
    return coordinates

def coor_2(n,a,b):
    """
    Calculates a list of coordinates using a list comprehension
    """
    length = (b-a)/float(n+1)
    coordinates = [a + length * (i + 1) for i in range(n+1)]
    return coordinates

def test_coor():
    """
    Using nosetests framework, tests the function coor for the case (3,1,5)
    """
    test = coor(3,1,5)
    case = [2.0,3.0,4.0]
    for i in range(3):
        n.tools.assert_almost_equal(case[i], test[i])

def main():
    """
    Prints the result of the case (3,1,5) using first coor, then coor_2
    """
    print coor(3,1,5)

if __name__ == "__main__":
    main()

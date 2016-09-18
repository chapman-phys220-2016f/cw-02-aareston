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

<<<<<<< HEAD
if __name__ == "__main__":
    main()
=======
coor(3,1,4)

### INSTRUCTOR COMMENTS
#
# Use docstrings properly. Leaving the template unaltered is a bad sign.
# Treat your work professionally. Would you show this file to a future
# employer? If not, it needs work.
# Your functions should also have docstrings. Remember, these docstrings
# are used by the python help system (using help() in an interpreter)
# so should follow standard python conventions for how to write documentation
# for functions and modules. When in doubt, just look at examples of existing
# functions in the interpreter.
#
# Try to use xrange instead of range when possible. xrange is a generator,
# so takes up little memory. range returns a full list in memory, which wastes
# memory if you don't need to reference the entire list at once.
#
# If you find yourself using list.append(item), consider using a list comprehension
# instead. For example:
#   coordinates = [a + length * i for i in xrange(n+1)]
#
# Do not put executable code (the last line) in your modules. You should write
# test functions instead, which can be run by the "nosetests" program in a
# terminal automatically. If you wish to run your module as a script, protect any
# executable code inside an if __name__ == "__main__" block.
>>>>>>> 8c37185826ff85b97c386813dd8c33239626f212

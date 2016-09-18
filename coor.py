#!/usr/bin/env python

"""Module Description
The docstring at the top of the file appears in the "Description" field of 
the help command. That is, if you load a python interpreter the following 
makes the docstring visible:

  $ python
  >>> import your_module
  >>> help(your_module)

Note the name "your_module" is just the filename without the .py extension.
You can check this field for any other python module (numpy, sympy, etc.) 
to get an idea about how module documentation is usually handled.
"""


def coor(n,a,b):
    coordinates = []
    length = (b-a)/float(n)
    for i in range(n+1):
        coordinates.append(a + length*i)
    for i in range(n+1):
        print coordinates[i]
    return 0

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

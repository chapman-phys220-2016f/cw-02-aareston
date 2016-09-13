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

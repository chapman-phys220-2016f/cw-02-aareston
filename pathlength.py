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

import math

def pathlength(x,y):
num = len(x)
eq = math.sqrt((x[i]-x[i-1])**2+(y[i]-y[i-1])**2)
L = sum(eq)
return L

def test_pathlength():
points = [(0,0), (0,3), (3,3) (3,0)]

num = len(points)
x = [points[i][0]]
y = [points[i][1]]

def test_pathlength():
points = [(0,0), (0,3), (3,3), (3,0)]

test = test_pathlength():
print test


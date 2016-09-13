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

import nose as n
import math

def pathlength(x,y):
    num = len(x)
    S = 0
    for i in range(num):
        S += math.sqrt((x[i]-x[i-1])**2+(y[i]-y[i-1])**2)
    return S


def test_pathlength():
    points = [(0,0), (0,3), (3,3), (3,0)]
    x = [p[0] for p in points]
    y = [p[1] for p in points]
    test = pathlength(x,y)
    case = 12.0
    n.tools.assert_almost_equal(test, case)


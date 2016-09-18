#!bin/usr/env python

import nose as n

"""
This module includes a function kinematics which computes the approximate velocity and acceleration of a point given it's position at a set of times.
"""

def kinematics(x, t):
    """Kinematics takes two lists as arguments, the first of positions, the second of times"""
    v = []
    a = []
    if len(x) != len(t):
        print "Invalid input. The lengths of the provided arguments must be equal"
    for i in range(len(x)):
        if i == 0:
            v.append("*")
            a.append("*")
        elif i == len(x):
            v.append("*")
            a.append("*")
        else:
            v.append((x[i + 1] - x[i - 1]) / (t[i + 1] - t[i - 1]))
            a.append(2 / (t[i + 1] - t[i - 1]) * ((x[i + 1] - x[i - 1]) / (t[i + 1] - t[i]) - (x[i] - x[i - 1]) / (t[i] - t[i - 1])))
    return v, a

def main():
    """Runs the function kinematics for x = t = [0, 0.5, 1.5, 2.2]. This implies a constant velocity and zero acceleration. The finite approximation used should match exactly the constant velocity of 1"""
    print kinematics([0, 0.5, 1.5, 2.2], [0, 0.5, 1.5, 2.2])

def test_kinematics():
    test = kinematics([0, 0.5, 1.5, 2.2], [0, 0.5, 1.5, 2.2])
    case = (["*",1.0,1.0,"*"], ["*",0.0,0.0,"*"])
    n.tools.assert_almost_equals(test, case, places=5)

if __name__ == "__main":
    main()

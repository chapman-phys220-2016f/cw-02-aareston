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
        if i == 0:              #These first two statements I added to take care of index out of bounds errors, but I'm still getting them.
            v.append("*")
            a.append("*")
        elif i == len(x) - 1:
            v.append("*")
            a.append("*")
        else:
            v.append((x[i + 1] - x[i - 1]) / (float(t[i + 1]) - t[i - 1]))
            a.append(2.0 / (t[i + 1] - t[i - 1]) * ((x[i + 1] - x[i - 1]) / (t[i + 1] - t[i]) - (x[i] - x[i - 1]) / (t[i] - t[i - 1])))
    return v, a

def main():
    """Runs the function kinematics for x = t = [0, 0.5, 1.5, 2.2]. This implies a constant velocity and zero acceleration. The finite approximation used should match exactly the constant velocity of 1"""
    print kinematics([0, 0.5, 1.5, 2.2], [0, 0.5, 1.5, 2.2])

def test_kinematics():
    test = kinematics([0, 0.5, 1.5, 2.2], [0, 0.5, 1.5, 2.2])
    case = (["*",1.0,1.0,"*"], ["*",0.0,0.0,"*"])               #This is going to cause issues, but to find velocity and acceleration values at the endpoints would require additional datapoints in x

    success = 0
    def approx_eq(x,y,tol=0.01):
        return abs(x - y) < tol
    for i, j in test, case:
        if approx_eq(i, j):
            success += 1
    assert(success == 4)

if __name__ == "__main":
    main()

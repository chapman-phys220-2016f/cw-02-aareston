#!bin/usr/env python

"""

"""

def kinematics(x, i, dt=1.0E-6):
#    if i == 0
#        return -1
#    elif i == x.len()
#        return -1
#    else
        ti_next  = (i + 1) * dt
        ti_now = i * dt
        ti_prev = (i - 1) * dt
        vi = (x[i + 1] - x[i - 1]) / (ti_next - ti_prev)
        ai = 2 / (ti_next - ti_prev) * ((x[i + 1] - x[i - 1]) / (ti_next - ti_now) - (x[i] - x[i - 1]) / (ti_now - ti_prev))
        return vi, ai

def main():
    print kinematics([1,2,3,4,5],1)

if __name__ == "__main":
    main()

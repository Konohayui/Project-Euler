# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 17:12:59 2017

@author: yu
"""

'''
Test for Pentagonal number: 
    1) n = (sqrt(24x+1)+1)/6 where x is a pentagonal number
    2) sqrt(24x+1) mod 6 equals to 5
'''

def is_Pentagonal(x):
    if (24*x+1)**(1/2)  % 6 == 5:
        return True

'''
Test for Hexagonal number: 
    n = (sqrt(8x+1)+1)/4 where x is a pentagonal number
'''
def is_Hexagonal(x):
    if ((8*x+1)**(1/2) + 1)/4 % 1 == 0:
        return True

def Triangular():
    T = []
    n = 1
    while len(T) < 3:
        t = (n*(n+1))/2
        if is_Pentagonal(t) and is_Hexagonal(t):
            T.append([t, n])
        n += 1
    return T

print(Triangular())




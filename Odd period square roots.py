# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 14:14:49 2017

@author: yu
"""

'''
Algorithm: https://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Continued_fraction_expansion
'''
from math import sqrt, floor

L = 10000
odd_period = 0
odd_period_num = []

for N in range(2, L + 1):
    s = initial = floor(sqrt(N))
    if s**2 != N: # check if N is a perfect square 
        triplet = []
        m, d, period = 0, 1, 0
        while s != 2*initial or (m,d,s) not in triplet:
            m = d*s - m
            d = (N - m**2) // d
            s = (initial + m) // d
            triplet = triplet + [(m, d, s)]
            period += 1
        if period % 2 != 0:
            odd_period += 1
            odd_period_num = odd_period_num + [N]
            
            
print(odd_period)


# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 13:54:47 2017

@author: yu
"""

'''
P_j and P_k are pentagonal number.
Let S be the sum of P_j and P_k,
let D be the difference of P_j and P_k,
if P_j + P_k = S and P_j - P_k = D are Pentagonal numbers, 
we have S - P_k = P_j or P_k = S - P_j is a Pentagonal numer.
Similarly, P_j = D + P_k is a Pentagonal number.
We have S - P_k = D + P_k which equivalent to D = S - 2P_k
where D is a Pentagonal number.
'''


'''
Test for Pentagonal number: 
    1) n = (sqrt(24x+1)+1)/6 where x is a pentagonal number
    2) sqrt(24x+1) mod 6 equals to 5
'''


# the index is 2395
def Pentagon():
    P = set()
    n = 1
    while True:
        S = (n*(3*n - 1))/2
        for k in range(1, n):
            P_k = (k*(3*k - 1))/2
            P_j = S - P_k
            D = S - 2*P_k
            if P_j in P and D in P:
                return P_j, P_k, S, D, n, k
        P.add(S)
        n += 1

                
print(Pentagon())


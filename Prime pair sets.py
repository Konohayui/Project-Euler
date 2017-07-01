# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 14:09:15 2017

@author: yu
"""

import itertools as itert
import random

def prime_sieve(n):
    primes = [True]*n
    for num in range(3,int(n**(1/2)), 2):
        if primes[num]:
            primes[num*num:n:2*num] = [False]*int((n-num*num-1)/(2*num) + 1)
    return [2] + [i for i in range(3, n, 2) if primes[i]]


'''
Wilson's theorem to determine whether an integer is a prime
Theorem: an integer n is a prime iff (n-1)! = -1 mod(n) 

Fermat's little theorem: a^p = a mod(p), p is a prime
'''

#def is_prime(n):
#    n = int(n)
#    if 2**(n - 1) % n == 1:
#        return True
    
# Miller–Rabin primality test
# One of the best algorithm to check if the given number if prime
# https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test
# Algorithm: http://bit.ly/2drtk0x

def is_prime(n, k = 3):
   n = int(n) 
   if n < 6:  # assuming n >= 0 in all cases... shortcut small cases here
      return [False, False, True, True, False, True][n]
   elif n % 2 == 0:  # should be faster than n % 2
      return False
   else:
      s, d = 0, n - 1
      while d % 2 == 0:
         s, d = s + 1, d >> 1
      # A for loop with a random sample of numbers
      for a in random.sample(range(2, n-2), k):
         x = pow(a, d, n)
         if x != 1 and x + 1 != n:
            for r in range(1, s):
               x = pow(x, 2, n)
               if x == 1:
                  return False  # composite for sure
               elif x == n - 1:
                  a = 0  # so we know loop didn't continue to end
                  break  # could be strong liar, try another a
            if a:
               return False  # composite if we reached end of this loop
      return True  # probably prime if reached end of outer loop
        
  
    
def are_all_primes(chain):
    return all(is_prime(str(p[0]) + str(p[1])) for p in itert.permutations(chain, 2))
    
primes = prime_sieve(10000)    

'''
Main Calculation:
'''

def prime_pair():
    result = []
    for p1 in primes:
        for p2 in primes:
            if p2 < p1:
                continue
            if are_all_primes([p1, p2]):
                result.append(p1) 
                result.append(p2)
                for p3 in primes:
                    if p3 < p2:
                        continue
                    if are_all_primes(result + [p3]):
                        result.append(p3)
                        for p4 in primes:
                            if p4 < p3:
                                continue
                            if are_all_primes(result + [p4]):
                                result.append(p4)
                                return sum(result), result
#
#                            
# need to come up with a good way to determine large prime number 
#
#                            
#                                for p5 in primes:
#                                    if p5 < p4:
#                                        continue
#                                    if are_all_primes(result + [p5]):
#                                        result.append(p5)
#                                        return sum(result), result
                            
print(prime_pair())
    
    




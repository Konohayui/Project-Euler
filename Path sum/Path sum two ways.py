# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 14:20:47 2017

@author: yu
"""

with open("p081_matrix.txt") as data:
    matrix = [[int(x) for x in line.split(',')] for line in data]
    
m = n = len(matrix)

for row in range(m):
    for col in range(n):
        if row == col == 0:
            matrix[row][col] += 0
        elif row == 0:
            matrix[row][col] += matrix[row][col - 1]
        elif col == 0:
            matrix[row][col] += matrix[row - 1][col]
        else:
            matrix[row][col] += min(matrix[row][col - 1], matrix[row - 1][col])

print(matrix[m-1][n-1])

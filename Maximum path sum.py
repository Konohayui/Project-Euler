# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 14:56:08 2017

@author: yu
"""

triangle1 = [[75],
             [95, 64],
             [17, 47, 82],
             [18, 35, 87, 10],
             [20,  4, 82, 47, 65],
             [19,  1, 23, 75,  3, 34],
             [88,  2, 77, 73,  7, 63, 67],
             [99, 65,  4, 28,  6, 16, 70, 92],
             [41, 41, 26, 56, 83, 40, 80, 70, 33],
             [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
             [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
             [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
             [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
             [63, 66,  4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
             [ 4, 62, 98, 27, 23,  9, 70, 98, 73, 93, 38, 53, 60,  4, 23]]

with open("p067_triangle.txt") as data:
    triangle2 = [[int(x) for x in line.split()] for line in data]

def path_sum(triangle):    
    for row in range(len(triangle)-1, 0, -1):
        for col in range(0, row):
            triangle[row - 1][col] += max(triangle[row][col], triangle[row][col + 1])
    return triangle[0][0]
        

print(path_sum(triangle1))
print(path_sum(triangle2))
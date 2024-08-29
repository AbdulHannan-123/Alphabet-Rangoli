#!/bin/python3

import math
import os
import random
import re
import sys




first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)
    
combined_string = ''

# Loop over each column index
for i in range(m):
    for row in matrix:
        combined_string += row[i]

#print(combined_string)

finalans = re.sub(r'(?<=\w)([^\w]+)(?=\w)', ' ', combined_string)

print(finalans)

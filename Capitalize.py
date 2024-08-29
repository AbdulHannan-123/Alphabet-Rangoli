#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    final_text=  ''
    for character in range(len(s)):
        if s[character-1] == ' ' or character == 0: 
            final_text += s[character].upper()
        else:
            final_text += s[character]
    return final_text

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()

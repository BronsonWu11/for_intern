'''
    A generator expression is similar to a list comprehension, but it creates
    a generator object of instead of a list. Generator are iterable, so you
    can loop through their values, but they do not store all values in memory
    at once. This makes them more memory-efficient when dealing with large datasets
    or infinite sequences. generator expressions use round parathese() instead of 
    square brackets[].
    Below is the hourglass problem
'''

# Solution 1(normal):
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def hourglassSum(arr):
    # Write your code here
    max_sum = -float('inf')
    for i in range(len(arr)-2):
        for j in range(len(arr[i])-2):
            hourglass = (
                arr[i][j] + arr[i][j+1] + arr[i][j+2] +
                arr[i+1][j+1] +
                arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            )
            max_sum = max(max_sum, hourglass)
    return max_sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

# Solution 2 (Generator Expression):
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def hourglassSum_GE(arr):
    # Write your code here
    return max(arr[i][j] + arr[i][j+1] + arr[i][j+2] + 
               arr[i+1][j+1] + 
               arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
               for i in range(4)
               for j in range(4)
    )

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

#!/usr/bin/python3
# FizzBuzz!IM

import sys

try:
    limit = sys.argv[1]
except IndexError:
    limit = input("Enter the limit for the range in this program: ")

for n in range(1, int(limit)):
    if (n % 3 == 0) and (n % 5 == 0):
        print("FizzBuzz!")
    elif n % 3 == 0:
        print("Fizz!")
    elif n % 5 == 0:
        print("Buzz!")
    else:
        print(n)
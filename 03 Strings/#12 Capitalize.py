"""

Problem URL:
https://www.hackerrank.com/challenges/capitalize/problem?isFullScreen=true

Task:
You are asked to ensure that the first and last names of people begin with a capital letter in their passports.
For example, alison heck should be capitalised correctly as Alison Heck.
alison heck => Alison Heck

Given a full name, your task is to capitalize the name appropriately

"""

#!/bin/python3


import os


# Complete the solve function below.
def solve(s):

    s = s.split(" ")
    s = [i.capitalize() for i in s]
    return " ".join(s)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()

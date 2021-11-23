"""

Problem URL:
https://www.hackerrank.com/challenges/python-string-formatting/problem?isFullScreen=true

Task:
Given an integer,n , print the following values for each integer i from 1 to n:

Decimal
Octal
Hexadecimal (capitalized)
Binary

Note:
The four values must be printed on a single line in the order specified above for each i from 1 to number.
Each value should be space-padded to match the width of the binary value of number
and the values should be separated by a single space.

"""


def print_formatted(number):
    width = len("{0:b}".format(number))
    for i in range(1, number + 1):
        print("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i, width=width))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
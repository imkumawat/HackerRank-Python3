"""

Problem URL:
https://www.hackerrank.com/challenges/python-loops/problem?isFullScreen=true

Task:
The provided code stub reads and integer, , from STDIN. For all non-negative integers
i<n print i*i

"""

if __name__ == '__main__':
    n = int(input())

    for i in range(n):
        print(i * i)
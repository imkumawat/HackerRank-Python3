"""

Problem URL:
https://www.hackerrank.com/challenges/designer-door-mat/problem?isFullScreen=true

Task:
Mr. Vincent works in a door mat manufacturing company.
One day, he designed a new door mat with the following specifications:

Mat size must be NxM. (N is an odd natural number, and M is 3 times N.)
The design should have 'WELCOME' written in the center.
The design pattern should only use |, . and - characters.

"""

height, length = map(int, input().split())
for i in range(0, height // 2):
    s = '.|.' * (i * 2 + 1)
    print(s.center(length,'-'))
print('WELCOME'.center(length, '-'))
for i in range(height // 2 - 1, -1, -1):
    s = '.|.' * (i * 2 + 1)
    print(s.center(length,'-'))
    
"""

Problem URL:
https://www.hackerrank.com/challenges/string-validators/problem?isFullScreen=true

Task:
You are given a string S.
Your task is to find out if the string S contains:
alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.
"""

if __name__ == '__main__':
    s = input()
    print(any(x.isalnum() for x in s))
    print(any(x.isalpha() for x in s))
    print(any(x.isdigit() for x in s))
    print(any(x.islower() for x in s))
    print(any(x.isupper() for x in s))
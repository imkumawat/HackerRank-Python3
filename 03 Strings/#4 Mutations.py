"""

Problem URL:
https://www.hackerrank.com/challenges/python-mutations/problem?isFullScreen=true

Task:
Read a given string, change the character at a given index and then print
the modified string.
"""

def mutate_string(string, position, character):
    stringlist = list(string)
    stringlist[position] = character
    string = ''.join(stringlist)
    return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
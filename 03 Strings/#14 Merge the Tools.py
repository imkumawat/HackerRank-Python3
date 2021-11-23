"""

Problem URL:
https://www.hackerrank.com/challenges/merge-the-tools/problem?isFullScreen=true

Task:
Consider the following:

A string, S, of length N where S = c0c1....cN-1.
An integer, K, where K is a factor of N.
We can split S into N/K substrings where each subtring, Ti,
consists of a contiguous block of K characters in S.
Then, use each Ti to create string Ui such that:

The characters in Ui are a subsequence of the characters in Ti.
Any repeat occurrence of a character is removed from the string
such that each character in Ui occurs exactly once. In other words,
if the character at some index j in Ti occurs at a previous index <j in Ti,
then do not include the character in string Ui.
Given S and K, print N/K lines where each line i denotes string Ui.

"""

from collections import OrderedDict
def merge_the_tools(string, k):
    for i in range(0, len(string)-k+1, k):
        print(''.join(OrderedDict.fromkeys(string[i:i + k])))
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

"""

Problem URL:
https://www.hackerrank.com/challenges/the-minion-game/problem?isFullScreen=true

Task:
Kevin and Stuart want to play the 'The Minion Game'.

Game Rules

Both players are given the same string, S.
Both players have to make substrings using the letters of the string S.
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.

Scoring
A player gets +1 point for each occurrence of the substring in the string S.

"""

def minion_game(string):
    s = string
    s_length = len(s)
    vowel_list = ['A','E','I','O','U']
    stuart_point = 0
    kevin_point = 0
    for i in range(s_length):
        if s[i] in vowel_list:
            kevin_point += s_length - i
        else:
            stuart_point += s_length - i
    if stuart_point == kevin_point:
        print('Draw')
    elif kevin_point > stuart_point:
        print('Kevin',kevin_point)
    else:
        print('Stuart',stuart_point)
if __name__ == '__main__':
    s = input()
    minion_game(s)
    
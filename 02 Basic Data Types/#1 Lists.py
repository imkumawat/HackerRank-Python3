"""
Problem URL:
https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true
Task:
Consider a list (list = []). You can perform the following commands:
insert i e: Insert integer e at position i.
print: Print the list.
remove e: Delete the first occurrence of integer e.
append e: Insert integer e at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of n followed by n lines of
commands where each command will be of the 7 types listed above.
Iterate through each command in order and perform the corresponding operation on your list.
"""

if __name__ == '__main__':
    N = int(input())
    list = []
    for i in range(N):

        command = input()

        cmd = command.split(" ")
        exe = cmd[0]

        if exe == 'insert':
            index = int(cmd[1])
            val = int(cmd[2])
            list.insert(index, val)

        if exe == 'print':
            print(list)

        if exe == 'remove':
            list.remove(int(cmd[1]))

        if exe == 'append':
            list.append(int(cmd[1]))

        if exe == 'sort':
            list.sort()

        if exe == 'pop':
            list.pop()

        if exe == 'reverse':
            list.reverse()

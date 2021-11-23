"""

Problem URL:
https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true

Task:
Given the names and grades for each student in a class of N students,
store them in a nested list and print the name(s) of any student(s)
having the second lowest grade.

Note: If there are multiple students with the second lowest grade,
order their names alphabetically and print each name on a new line.

"""

if __name__ == '__main__':
    data = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        data.append([name, score])

    second_lowest = sorted(list(set([score for name, score in data])))[1]

    print('\n'.join([name for name, score in sorted(data) if score == second_lowest]))

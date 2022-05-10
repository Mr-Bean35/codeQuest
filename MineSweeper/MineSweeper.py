# File : MineSweeper.py
# Date : 2/28/2022
# Author : Ben Hensley Jr.

with open('MineSweeper.txt') as f:
    next(f)
    lines = [line.strip().split() for line in f]


print(lines)

for line in lines:
    if len(line) == 3:
        GridA = line[0] * int(line[1])
        GridX = 0
        GridY = 0
        if GridX == line[0] and GridY == line[1]:
            End = End + '*'
        else:
            print(End)



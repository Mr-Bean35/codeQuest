# File : Fib.py
# Date : 2/28/2022
# Author : Ben Hensley Jr.

with open('Fib.txt') as f:
    next(f)
    lines = f.readlines()


Pos1 = 0
Pos2 = 1
Space = 0
CNT = 0

for line in lines:
    line = int(line)
    while line > CNT:
        Space = list(Pos2).copy()
        Pos2 = Pos1 + Pos2
        CNT += 1
        Pos1 = Space.copy()
        Pos1 = int(Space)
        if line == CNT:
            print(f'{line} = {Pos1}')











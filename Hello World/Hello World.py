# File : Hello World.py
# Date : 2/28/2022
# Author : Ben Hensley Jr.

with open('Hello World.txt') as f:
    next(f)
    lines = [line.strip() for line in f]

for line in lines:
    print(line)

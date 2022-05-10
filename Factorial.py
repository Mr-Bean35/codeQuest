# File : Factorial.py
# Date : 2/16/2022
# Author : Ben Hensley Jr.

with open('Text.txt') as f:
    line = f.read()
    line = [line.strip() for line in line]
    while '' in line:
        line.remove('')



ST2 = 1
CNT = 0

X = line[CNT]
X = int(X)
CNT += 1
Y = line[CNT]
Y = int(Y)
X = (X * Y)
print(X)
while len(line)-1 > ST2:
    CNT += 1
    Z = line[CNT]
    Z = int(Z)
    X = (X * Z)
    print(X)
    ST2 += 1









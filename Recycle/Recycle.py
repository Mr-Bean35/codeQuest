# File : Recycle.py
# Date : 2/24/2022
# Author : Ben Hensley Jr.


with open('Text.txt') as f:
    next(f)
    lines = [line.strip().split() for line in f]

for line in lines:
    Alum_lbs = float(line[0])
    Plastic_lbs = float(line[1])
    Glass_lbs = float(line[2])

    Alum_Cnt = 31 * Alum_lbs
    Plas_Cnt = 15 * Plastic_lbs
    Glass_Cnt = 0.5 * Glass_lbs

    Alum_Mon = 0.05 * Alum_Cnt
    Plas_Mon = 0.10 * Plas_Cnt
    Glass_Mon = 0.20 * Glass_Cnt

    Amount = Alum_Mon + Plas_Mon + Glass_Mon
    End = '${:.2f}'
    print(End.format(Amount))








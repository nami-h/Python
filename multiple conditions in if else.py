#!/bin/python3

import os
import sys

#
# Complete the gradingStudents function below.
#
def gradingStudents(grades):
    l=[]
    for i in grades:
        if i<38:
            l.append(i)
        elif i%5==1 or i%5==2 or i%5==0:
            l.append(i)
        elif i%5==3:
            l.append(i+2)
        elif i%5==4:
            l.append(i+1)
    return l

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grades = []

    for _ in range(n):
        grades_item = int(input())
        grades.append(grades_item)

    result = gradingStudents(grades)

    f.write('\n'.join(map(str, result)))
    f.write('\n')

    f.close()

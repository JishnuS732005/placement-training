#  https://www.hackerrank.com/challenges/py-collections-namedtuple/problem?isFullScreen=true

from collections import namedtuple
import sys
input = sys.stdin.read
data=input().strip().split('\n')
n=int(data[0])
header=data[1].split()
Student=namedtuple('Student',header)
marks=[int(Student._make(line.split()).MARKS)for line in data[2:]]

print(f"{sum(marks)/len(marks):.2f}")

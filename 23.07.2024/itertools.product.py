#  https://www.hackerrank.com/challenges/itertools-product/problem?isFullScreen=true

from itertools import product
A=list(map(int,input().split()))
B=list(map(int,input().split()))
cartesian_product=product(A,B)
print(' '.join(map(str,cartesian_product)))

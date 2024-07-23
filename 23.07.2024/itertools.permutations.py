#  https://www.hackerrank.com/challenges/itertools-permutations/problem?isFullScreen=true

from itertools import permutations
input_str,k = input().split()
k=int(k)
perm=permutations(sorted(input_str),k)
for p in perm:
    print(''.join(p))

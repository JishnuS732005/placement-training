#  https://www.hackerrank.com/challenges/itertools-combinations/problem?isFullScreen=true

from itertools import combinations
input_str,k = input().split()
k=int(k)
sorted_str=sorted(input_str)
for i in range(1,k+1):
    for comb in combinations(sorted_str,i):
        print(''.join(comb))

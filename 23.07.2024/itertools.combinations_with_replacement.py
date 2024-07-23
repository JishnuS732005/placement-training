#  https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem?isFullScreen=true

from itertools import combinations_with_replacement
input_str,k = input().split()
k=int(k)
sorted_str=sorted(input_str)
for comb in combinations_with_replacement(sorted_str,k):
    print(''.join(comb))

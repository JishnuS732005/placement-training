#  https://www.hackerrank.com/challenges/defaultdict-tutorial/problem?isFullScreen=true

from collections import defaultdict
n,m=map(int,input().split())
indices=defaultdict(list)
for i in range(1,n+1):
    word=input().strip()
    indices[word].append(i)
for _ in range(m):
    word=input().strip()
    if word in indices:
        print(" ".join(map(str,indices[word])))
    else:
        print(-1)

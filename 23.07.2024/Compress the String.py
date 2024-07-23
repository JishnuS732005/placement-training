#  https://www.hackerrank.com/challenges/compress-the-string/problem?isFullScreen=true

from itertools import groupby
s=input()
result=[(len(list(g)),int(k))for k,g in groupby(s)]
print(' '.join(str(item)for item in result))

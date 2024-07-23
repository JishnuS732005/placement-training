#  https://www.hackerrank.com/challenges/word-order/problem?isFullScreen=true

from collections import OrderedDict
import sys
if __name__ == '__main__':
    input=sys.stdin.read
    data=input().splitlines()
    n=int(data[0])
    words=data[1:]
    word_count=OrderedDict()
    for word in words:
        if word in word_count:
            word_count[word]+=1
        else:
            word_count[word]=1
    print(len(word_count))
    print(' '.join(map(str,word_count.values())))

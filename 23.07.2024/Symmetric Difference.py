#  https://www.hackerrank.com/challenges/symmetric-difference/problem?isFullScreen=true

if __name__ == '__main__':
    M=int(input())
    set_a=set(map(int,input().split()))
    N=int(input())
    set_b=set(map(int,input().split()))
    symmetric_difference=set_a.symmetric_difference(set_b)
    result=sorted(symmetric_difference)
    for element in result:
        print(element)

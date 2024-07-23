#  https://www.hackerrank.com/challenges/no-idea/problem?isFullScreen=true

if __name__ == '__main__':
    n,m=map(int,input().split())
    array=list(map(int,input().split()))
    set_A=set(map(int,input().split()))
    set_B=set(map(int,input().split()))
    happiness=0
    for element in array:
        if element in set_A:
            happiness += 1
        elif element in set_B:
            happiness -= 1
    print(happiness)

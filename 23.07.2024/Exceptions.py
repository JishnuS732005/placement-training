#  https://www.hackerrank.com/challenges/exceptions/problem?isFullScreen=true

t=int(input().strip())
for _ in range(t):
    try:
        a,b=input().split()
        result=int(a)//int(b)
        print(result)
    except ZeroDivisionError as e:
        print("Error Code:",e)
    except ValueError as e:
        print("Error Code:",e)

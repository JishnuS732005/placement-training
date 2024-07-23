#  https://www.hackerrank.com/challenges/py-introduction-to-sets/problem?isFullScreen=true

def average(array):
    distinct_elements=set(array)
    total_sum=sum(distinct_elements)
    num_elements=len(distinct_elements)
    avg=total_sum/num_elements
    return avg

if _name_ == '_main_':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)

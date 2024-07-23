#  https://www.hackerrank.com/challenges/collections-counter/problem?isFullScreen=true

from collections import Counter
number_of_shoes=int(input())
shoe_sizes=list(map(int,input().split()))
number_of_customers=int(input())
inventory=Counter(shoe_sizes)
total_earnings=0
for _ in range(number_of_customers):
    size,price = map(int,input().split())
    if inventory[size]>0:
        total_earnings+=price
        inventory[size]-=1
        
print(total_earnings)

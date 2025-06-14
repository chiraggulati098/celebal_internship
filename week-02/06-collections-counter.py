# https://www.hackerrank.com/challenges/collections-counter/problem?isFullScreen=true

from collections import Counter

num_shoes = int(input())
shoes = Counter(list(map(int, input().split())))

num_cust = int(input())
res = 0

for _ in range(num_cust):
    size, price = map(int, input().split())
    
    if shoes[size] > 0:
        res += price
        shoes[size] -= 1

print(res)
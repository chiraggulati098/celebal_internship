# https://www.hackerrank.com/challenges/iterables-and-iterators/problem?isFullScreen=true

from itertools import combinations

n = int(input())
alphabets = input().split()
k = int(input())

tups = list(combinations(alphabets, k))

res = sum([1 for tup in tups if 'a' in tup]) / len(tups)
print(res)
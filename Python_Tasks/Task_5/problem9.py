# Problem 9: Word Order
# HackerRank: https://www.hackerrank.com/challenges/word-order/problem

from collections import OrderedDict
n=int(input())
counts=OrderedDict()
for _ in range(n):
    word=input().strip()
    counts[word]=counts.get(word,0)+1
print(len(counts))
print(*counts.values())

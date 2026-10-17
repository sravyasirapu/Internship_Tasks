# Problem 15: Game of Thrones - I
# HackerRank: https://www.hackerrank.com/challenges/game-of-thrones/problem

from collections import Counter

print("YES" if sum(v % 2 for v in Counter(input().strip()).values()) <= 1 else "NO")
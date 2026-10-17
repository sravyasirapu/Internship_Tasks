# Problem 19: Weighted Uniform Strings
# HackerRank: https://www.hackerrank.com/challenges/weighted-uniform-string/problem


s = input().strip()
q = int(input())

weights = set()
prev = ""
count = 0

for c in s:
    count = count + 1 if c == prev else 1
    prev = c
    weights.add((ord(c) - 96) * count)

for _ in range(q):
    print("Yes" if int(input()) in weights else "No")

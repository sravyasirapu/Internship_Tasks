# Problem 10: CamelCase
# HackerRank: https://www.hackerrank.com/challenges/camelcase/problem

s=input().strip()
print(0 if not s else 1+sum(c.isupper() for c in s))

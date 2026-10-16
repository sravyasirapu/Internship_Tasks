# Problem 20: No Idea!
# HackerRank: https://www.hackerrank.com/challenges/no-idea/problem

n, m = map(int, input().split())
arr = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))
happiness = 0
for value in arr:
    if value in A:
        happiness += 1
    elif value in B:
        happiness -= 1
print(happiness)

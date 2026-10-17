# Problem 2: The Captain's Room
# HackerRank: https://www.hackerrank.com/challenges/py-the-captains-room/problem

n = int(input())
a = set(map(int, input().split()))

m = int(input())
b = set(map(int, input().split()))

print(len(a.symmetric_difference(b)))

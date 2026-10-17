# Problem 1: Set symmetric difference
# HackerRank: https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem

a=set(map(int,input().split()))
b=set(map(int,input().split()))
print(len(a^b))

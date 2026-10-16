# Problem 12: Introduction to Sets
# HackerRank: https://www.hackerrank.com/challenges/introduction-to-sets/problem

def average(array):
    unique = set(array)
    return sum(unique) / len(unique)

n = int(input())
arr = list(map(int, input().split()))
print(average(arr))

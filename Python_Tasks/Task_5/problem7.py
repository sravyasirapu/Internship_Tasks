# Problem 7: Symmetric Difference
# HackerRank: https://www.hackerrank.com/challenges/symmetric-difference/problem

m=int(input())
a=set(map(int,input().split()))
n=int(input())
b=set(map(int,input().split()))
print(*sorted(a.symmetric_difference(b)), sep="\n")


# another way

m = int(input())
set1 = set(map(int, input().split()))
n = int(input())
set2 = set(map(int, input().split()))
for value in sorted(set1.symmetric_difference(set2)):
    print(value)

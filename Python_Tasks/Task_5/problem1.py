# Problem 1: Find the Runner-Up Score!
# HackerRank: https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

if __name__ == '__main__':
    n=int(input())
scores=list(map(int,input().split()))
print(sorted(set(scores), reverse=True)[1])

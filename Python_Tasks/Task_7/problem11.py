# Problem 11: Two Strings
# HackerRank: https://www.hackerrank.com/challenges/two-strings/problem

for _ in range(int(input())):
 a=set(input().strip()); 
 b=set(input().strip())
 print("YES" if a&b else "NO")

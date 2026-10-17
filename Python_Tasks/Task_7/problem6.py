# Problem 6: Pangrams
# HackerRank: https://www.hackerrank.com/challenges/pangrams/problem

s=set(input().lower())
print("pangram" if set("abcdefghijklmnopqrstuvwxyz")<=s else "not pangram")

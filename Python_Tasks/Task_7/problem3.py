# Problem 3: Mars Exploration
# HackerRank: https://www.hackerrank.com/challenges/mars-exploration/problem

s=input().strip()
print(sum(c!="SOS"[i%3] for i,c in enumerate(s)))

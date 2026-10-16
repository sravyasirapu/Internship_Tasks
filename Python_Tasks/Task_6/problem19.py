# Problem 19: Company Logo
# HackerRank: https://www.hackerrank.com/challenges/most-commons/problem

from collections import Counter
s=input().strip()
for ch,count in sorted(Counter(s).items(),key=lambda x:(-x[1],x[0]))[:3]: print(ch,count)

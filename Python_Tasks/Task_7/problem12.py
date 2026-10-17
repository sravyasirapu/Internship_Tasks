# Problem 12: Making Anagrams
# HackerRank: https://www.hackerrank.com/challenges/making-anagrams/problem

from collections import Counter
a=Counter(input().strip()); 
b=Counter(input().strip())
print(sum((a-b).values())+sum((b-a).values()))

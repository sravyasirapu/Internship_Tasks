# Problem 13: Sherlock and the Valid String
# HackerRank: https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem


from collections import Counter

s = input().strip()
freq = Counter(Counter(s).values())

if len(freq) == 1:
    print("YES")
elif len(freq) == 2:
    (a, x), (b, y) = sorted(freq.items())
    if (a == 1 and x == 1) or (b == a + 1 and y == 1):
        print("YES")
    else:
        print("NO")
else:
    print("NO")


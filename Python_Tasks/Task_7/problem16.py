# Problem 16: Caesar Cipher
# HackerRank: https://www.hackerrank.com/challenges/caesar-cipher-1/problem


n = int(input())
s = input().strip()
k = int(input()) % 26

out = []

for c in s:
    if c.islower():
        out.append(chr((ord(c) - 97 + k) % 26 + 97))
    elif c.isupper():
        out.append(chr((ord(c) - 65 + k) % 26 + 65))
    else:
        out.append(c)

print("".join(out))

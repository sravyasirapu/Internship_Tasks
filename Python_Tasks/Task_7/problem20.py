# Problem 20: Super Reduced String
# HackerRank: https://www.hackerrank.com/challenges/reduced-string/problem


s = input().strip()
stack = []

for c in s:
    if stack and stack[-1] == c:
        stack.pop()
    else:
        stack.append(c)

r = "".join(stack)
print(r if r else "Empty String")

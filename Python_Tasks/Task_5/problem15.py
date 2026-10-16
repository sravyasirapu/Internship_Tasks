# Problem 15: Lists
# HackerRank: https://www.hackerrank.com/challenges/python-lists/problem

n=int(input())
items=[]
for _ in range(n):
    parts=input().split()
    cmd=parts[0]
    if cmd=="insert": items.insert(int(parts[1]),int(parts[2]))
    elif cmd=="print": print(items)
    elif cmd=="remove": items.remove(int(parts[1]))
    elif cmd=="append": items.append(int(parts[1]))
    elif cmd=="sort": items.sort()
    elif cmd=="pop": items.pop()
    elif cmd=="reverse": items.reverse()

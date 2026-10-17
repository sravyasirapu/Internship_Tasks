# Problem 4: Funny String
# HackerRank: https://www.hackerrank.com/challenges/funny-string/problem

for _ in range(int(input())):
 s=input().strip(); r=s[::-1]
 print("Funny" if all(abs(ord(s[i])-ord(s[i-1]))==abs(ord(r[i])-ord(r[i-1])) for i in range(1,len(s))) else "Not Funny")

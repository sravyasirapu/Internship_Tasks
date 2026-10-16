# Problem 14: Finding the Percentage
# HackerRank: https://www.hackerrank.com/challenges/finding-the-percentage/problem

n=int(input())
students={}
for _ in range(n):
    name,*marks=input().split()
    students[name]=list(map(float,marks))
query=input().strip()
print(f"{sum(students[query])/len(students[query]):.2f}")

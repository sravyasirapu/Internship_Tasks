# Problem 6: Introduction to Sets
# HackerRank: https://www.hackerrank.com/challenges/py-introduction-to-sets/problem

def average(array):
    values=set(array)
    return sum(values)/len(values)
if __name__ == "__main__":
    n=int(input())
    arr=list(map(int,input().split()))
    print(average(arr))

# Problem 19: Merge the Tools!
# HackerRank: https://www.hackerrank.com/challenges/merge-the-tools/problem

def merge_the_tools(string, k):
    for i in range(0,len(string),k):
        chunk=string[i:i+k]
        unique=""
        for char in chunk:
            if char not in unique: unique+=char
        print(unique)
if __name__ == "__main__":
    string=input()
    k=int(input())
    merge_the_tools(string,k)

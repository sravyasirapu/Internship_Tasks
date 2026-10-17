# Problem 17: Separate the Numbers
# HackerRank: https://www.hackerrank.com/challenges/separate-the-numbers/problem


for _ in range(int(input())):
    s = input().strip()
    found = False

    for l in range(1, len(s) // 2 + 1):
        first_str = s[:l]

        if first_str[0] == "0":
            continue

        first = int(first_str)
        cur = first
        built = ""

        while len(built) < len(s):
            built += str(cur)
            cur += 1

        if built == s:
            print("YES", first)
            found = True
            break

    if not found:
        print("NO")


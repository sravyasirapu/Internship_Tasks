# Problem 7: Alphabet Rangoli
# HackerRank: https://www.hackerrank.com/challenges/alphabet-rangoli/problem

import string

def rangoli(size):
    alpha = string.ascii_lowercase
    lines = []

    for i in range(size):
        left = "-".join(alpha[size-1:size-i-2:-1])
        right = "-".join(alpha[size-i-1:size])
        row = left + ("-" if left and right else "") + right
        lines.append(row.center(4 * size - 3, "-"))

    return "\n".join(lines[:0:-1] + lines)


if __name__ == '__main__':
    n = int(input())
    print(rangoli(n))


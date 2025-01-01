import sys, threading
input = sys.stdin.readline
from collections import defaultdict
input = sys.stdin.readline


def main():
    s = input().strip()
    t = input().strip()

    common_suffix_length = 0
    i = len(s) - 1
    j = len(t) - 1

    while i >= 0 and j >= 0 and s[i] == t[j]:
        common_suffix_length += 1
        i -= 1
        j -= 1

    total_length = len(s) + len(t)
    result = total_length - 2 * common_suffix_length
    return result

print(main())

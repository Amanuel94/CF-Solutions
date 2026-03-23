#!/usr/bin/env python3
from functools import cache
from itertools import accumulate
from bisect import bisect_left, bisect_right
from typing import List
import pdb

inf = float('inf')

def solve(ring, key):

    @cache
    def dp(i, j, k):
        nonlocal ring, key

        # breakpoint()
        if j == len(key):
            return 0

        i %= len(ring)
        c = 0
        while j < len(key) and ring[i] == key[j]:
            c += 1
            j += 1
        if c >= 1:
            return int(j < len(key)) + c + min(dp(i + 1, j, 1),
                        dp(i - 1, j, -1))

        return 1 + dp(i + k, j, k)

    return min(dp(0, 0, 1), dp(0, 0, -1))


# print(solve("godding", 'gd'))
# print(solve("godding", 'godding'))
# print(solve("aaaaa", 'aaaaa'))
# print(solve("edcba", "abcde"))
print(solve("fjdkfjdfkjd", "jjjkkkk"))



from typing import List
from functools import cache
from sortedcontainers import SortedList

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        # sort by  h, w
        # dp[i] =  longest subsequence starting at index i
        # 13 17 

        dp = [1] * len(envelopes)
        envelopes.sort(key=lambda e: (e[0], -e[1]))
        print(sorted(envelopes, key = lambda e: (e[0], -e[1])))
            

        # @cache
        # def dp(i, k):
        #     if i >= len(envelopes):
        #         return k


                



a = Solution().maxEnvelopes([[15,8],
                             [2,20],
                             [2,14],
                             [4,17],
                             [8,19],
                             [8,9],
                             [5,7],
                             [11,19],
                             [8,11],
                             [13,11],
                             [2,13],
                             [11,19],
                             [8,11],
                             [13,11],
                             [2,13],
                             [11,19],
                             [16,1],
                             [18,13],
                             [14,17],
                             [18,19]])
print(a)


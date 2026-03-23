#!/usr/bin/env python3
from functools import cache
from itertools import accumulate
from bisect import bisect_left, bisect_right
from typing import List

inf = float('inf')

def solve(board, hand):
    hand = ''.join(sorted(hand))
    def clean(board):
        stack = []
        i = 0
        while i < len(board):
            if stack and stack[-1] != board[i]:
                j = len(stack)-1
                count = 0

                while j > -1 and stack[j] == stack[-1]:
                    count += 1
                    j -= 1

                if count >= 3:
                    prev = stack[-1]
                    while stack and stack[-1] == prev:
                        stack.pop()
            stack.append(board[i])
            i += 1
                
        j = len(stack)-1
        count = 0

        while j > -1 and stack[j] == stack[-1]:
            count += 1
            j -= 1

        if count >= 3:
            prev = stack[-1]
            while stack and stack[-1] == prev:
                stack.pop()

        return "".join(stack)

    @cache
    def dp(board, mask):
        nonlocal hand
        board = clean(board)
        if not board:
            return len(hand) - len(mask)

        if not mask:
            return inf

        ans = inf
        for b in range(len(mask)):
            color = mask[b]
            i = 0 
            while i < len(board):
                if color == board[i] or i and board[i] == board[i-1]:
                    ans = min(ans, dp(
                        board[:i] + color + board[i:],
                        mask[:b] + mask[b+1:]
                    ))
                i += 1


        return ans


    board = clean(board)
    # res = dp(board, 2**(len(hand)) - 1)
    res = dp(board, hand)
    return res if res < inf else -1

print(solve("WRRBBW", "RB"))
print(solve("WWRRBBWW", "WRBRW"))
print(solve("G", "GGGGG"))
print(solve("RRWWRRBBRR", "WB"))
print(solve("WBBWW", "BRG"))
print(solve("RRYRRYYRYYRRYYRR", "YYRYY"))
print(solve("GWRBGYWGWGWYGRYW", "BRGGW"))

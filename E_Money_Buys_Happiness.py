import sys, threading
input = sys.stdin.readline
from collections import defaultdict
inf = float('inf')
# returns the first number where key becomes true for a given delegate type key
def bs(low=1, high=1, key = lambda x: True):

    while low <= high:
        mid = (low + high)//2
        if key(mid):
            high = mid-1
        else:
            low = mid+1
    return low


def main():
    t = int(input())
     
    for _ in range(t):
        m,  x =  list(map(int, input().split()))
        h = []
        c=  []
        for _ in range(m):
            ci, hi =  list(map(int, input().split()))
            h.append(hi)
            c.append(ci)
            #
        
        memo = {}
        def dp(i, e):
            nonlocal m, x
            if i >= m:
                return 0
            if (i, e) not in memo:
                memo[(i, e)] = max(
                    h[i] + dp(i+1, e - c[i] + x) if e - c[i] >= 0 else -inf,
                    dp(i+1, e + x)
                )
            return memo[(i, e)]
    

        print(dp(0, 0))

        # a b c d e
        # a b c d e
    


main()

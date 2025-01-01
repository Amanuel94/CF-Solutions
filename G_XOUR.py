from heapq import heappop, heappush
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
        n = int(input())
        a =  list(map(int, input().split()))
        grp = {}

        for i, ai in enumerate(a):
            k = str(ai >> 2)
            if k not in grp:
                grp[k] = []
            heappush(grp[k], ai)    
        ans = []
        # for i in range(n):
        #     k = str(a[i] >> 2)
        #     ans.append(heappop(grp[k]))
        print(*[heappop(grp[str(a[i] >> 2)]) for i in range(n)])


main()
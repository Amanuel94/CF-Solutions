import sys, threading
input = sys.stdin.readline
from collections import defaultdict
input = sys.stdin.readline

# returns the first number where key becomes true for a given delegate type key
def bs(low=1, high=1, key = lambda x: True):

    while low <= high:
        mid = (low + high)//2
        if key(mid):
            high = mid-1
        else:
            low = mid+1
    return low

def good(x, n, m):
    res = 0
    x -= 1
    for i in range(1, n + 1):
        res += min(m, x // i)
    return res



def main():
    n,m, k = map(int, input().split())
    low, high = 1, n * m + 1
    print(bs(low, high, lambda x: good(x, n, m) >= k)-1)


main()
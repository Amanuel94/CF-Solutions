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
    n, w =  list(map(int, input().split()))
    a = list(map(int, input().split()))

    pre = 0
    mn = 0
    mx = w
    for i in range(n):
        pre += a[i]
        if pre > w or pre < -w:
            print(0)
            return
    
        if pre >= 0:
            mx = min(mx, w - pre)
        else:
            mn = max(mn,  -pre)
        
    print(max(0, mx - mn + 1))


    



main()

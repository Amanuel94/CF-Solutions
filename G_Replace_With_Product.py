import sys, threading
input = sys.stdin.readline
from collections import defaultdict
input = sys.stdin.readline
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


def pref(a, pref, suf):
    
    l = 0
    while l < len(a) and a[l] == 1:
        l+=1
    r = l
    if l  == len(a): return l-1, r-1
    prod = a[l]
    ones = 0
    a_l, a_r = 0, 0
    p = -inf
    while l < len(a):
        while r < len(a) and a[r] == 1:
            r+=1
            ones += 1
        if r == len(a):
            return a_l, a_r
        if ones >= prod:
            l = r
        else:
            prod *= a[r]
            if pref[l-1] + prod + suf[r+1] > p:
                p = pref[l-1] + prod + suf[r+1]
                a_l, a_r = l, r
            r+=1
    return l, r





def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a =  list(map(int, input().split()))
        pre = [0]*n
        suf = [0]*n
        pre[0] += a[0]
        suf[-1] += a[-1] 
        for i in range(1, len(a)):
            pre[i] = a[i] + pre[i-1]
            suf[len(a) - 1 - i] = a[len(a)-1-i]  + suf[len(a) - i]
        
        prod = 1
        l = 0
        ones = 0
        r = len(a)
        while l < len(a):

        



# Wait for the main thread to complete
main()
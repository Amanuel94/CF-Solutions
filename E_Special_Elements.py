import sys, threading
input = sys.stdin.readline
from collections import defaultdict
inf = float('inf')
MOD = 10**9 + 7

def si():
    return input().strip()
def ii():
    return int(input())
def lsi():
    return input().strip().split()
def mi():
    return map(int, input().split())
def li():
    return list(map(int, input().split()))

def SieveOfEratosthenes(n):
    prime = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    prime[0]= False
    prime[1]= False
    return prime

def YN(b):
    return "YES" if b else "NO"

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
        n = ii()
        a = li()
        pref = [0]
        m = -inf
        mi = inf
        for ai in a:
            m = max(m, ai)
            mi = min(mi, ai)
            pref.append(pref[-1] + ai)
        count = [0]*(m - mi+1)
        for ai in a:
            count[ai - mi] += 1
        ans = 0
        for l in range(n+1):
            for r in range(l+2, n+1):
                if mi <= pref[r] - pref[l] <= m:
                    
                    ans += count[pref[r] - pref[l] - mi] 
                    count[pref[r] - pref[l] - mi]  = 0  
                if pref[r] - pref[l] > m:
                    break
        print(ans)

main()
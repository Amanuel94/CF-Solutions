from math import sqrt
import sys, threading
# input = sys.stdin.readline
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


# def cmp(A, )

def main():
    n, t = li()
    a = [-1] + li() + [-1]
    Qs = []
    for _ in range(t):
        l, r =  li()
        Qs.append((_, (l, r)))
        
    sqn = int(sqrt(n))
    ans = [0]*t
    freq = defaultdict(int)
    Qs.sort(key =lambda x: (x[1][0] // sqn, x[1][1] if (x[1][0] // sqn) % 2 == 0 else -x[1][1]))

    currL, currR = 1, 0
    currSum = 0
    for i, Q in Qs:
        l, r = Q
        
        while r >= currR:
            freq[a[currR]] += 1
            if freq[a[currR]] == a[currR]:
                currSum += 1
            if freq[a[currR]] == a[currR] + 1:
                currSum -= 1
            
            currR += 1
             
        while r+1 < currR:
            currR -= 1
            if freq[a[currR]] == a[currR]:
                currSum -= 1
            
            if freq[a[currR]] == a[currR] + 1:
                currSum += 1
            
            freq[a[currR]] -= 1
            
        while l > currL:
            if freq[a[currL]] == a[currL]:
                currSum -= 1
            if freq[a[currL]] == a[currL] + 1:
                currSum -= 1
            freq[a[currL]] -= 1
            currL+=1

        while l < currL:
            
            currL-=1
            freq[a[currL]] += 1
            if freq[a[currL]] == a[currL]:
                currSum += 1
            
            if freq[a[currL]] == a[currL] + 1:
                currSum -= 1
        
    
        ans[i] = str(currSum)
        
    print('\n'.join(ans))
    

main()
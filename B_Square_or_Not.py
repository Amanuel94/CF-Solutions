import math
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
    return "Yes" if b else "No"

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
        n = ii()
        s = si()
        m = int(math.sqrt(n))
        mat = [[0]*m for _ in range(m)]
        for i in range(n):
            r = i//m
            c = i%m
            if r > len(mat)-1: return False
            mat[r][c] = s[i]
        if '0' in mat[0] + mat[-1]:
            return False
        
        for i in range(1, m-1):
            if '0' in mat[i]:
                l = mat[i].index('0')
                r = mat[i][::-1].index('0')
                r = m - 1 - r
                if l == 0 or r == m-1 or "1" in mat[i][l:r]:
                    return False
            else:
                return False
        return True
t = int(input())
for _ in range(t):
    print(YN(main()))
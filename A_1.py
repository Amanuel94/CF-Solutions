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
# a b c d e f g h
# 
def bs(low=1, high=1, key = lambda x: True):
    while low <= high:
        mid = (low + high)//2
        if key(mid):
            high = mid-1
        else:
            low = mid+1
    return low

class Fenwick:

    def __init__(self, n, m):
        self.fenwicks = [[0] * (n + 1) for _ in range(m)]
        self.arr = [0] * n
        self.m = m

    def update(self, pos, val):
        if self.arr[pos - 1] + val < 0:
            return self.arr[pos - 1] 
        
        original_mod = self.arr[pos - 1] % self.m
        self._adjust(pos, -self.arr[pos - 1], original_mod)
        self.arr[pos - 1] += val
        new_mod = self.arr[pos - 1] % self.m
        self._adjust(pos, self.arr[pos - 1], new_mod)
        return self.arr[pos - 1]

    def _adjust(self, pos, val, mod):
        while pos < len(self.fenwicks[mod]):
            self.fenwicks[mod][pos] += val
            pos += pos & -pos

    def query(self, pos, mod):
        res = 0
        while pos > 0:
            res += self.fenwicks[mod][pos]
            pos -= pos & -pos
        return res

def main():
    n, m = li()
    fen = Fenwick(n, m)
    a = li()
    for i, ai in enumerate(a):
        fen.update(i + 1, ai)
    q = ii()
    for _ in range(q):
        qi = lsi()
        if qi[0] == "+":
            p, r = int(qi[1]), int(qi[2])
            print(fen.update(p, r))
        elif qi[0] == "-":
            p, r = int(qi[1]), int(qi[2])
            print(fen.update(p, -r))
        else:
            l, r, mod = int(qi[1]), int(qi[2]), int(qi[3])
            print(fen.query(r, mod) - fen.query(l - 1, mod))

if __name__ == "__main__":
    main()

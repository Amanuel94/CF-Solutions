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

class Fenwick:

    def __init__(self, n) -> None:
        self.fen = [0]*n
    
    def update(self, pos, val):
        while pos < len(self.fen):
            self.fen[pos] += val
            pos +=  pos & (-pos)
    def query(self, pos):
        ans = 0
        while pos > 0:
            ans += self.fen[pos]
            pos -=  pos & (-pos)
        return ans


def main():
    t = int(input())
    a = li()
    l = [0]*t
    r = [0]*t
    counter =  defaultdict(int)
    for i, ai in enumerate(a):
        counter[ai] += 1
        l[i] += counter[ai]
    counter = defaultdict(int)
    for i in range(t-1, -1, -1):
        counter[a[i]] += 1
        r[i] = counter[a[i]]

    fen = Fenwick(max(l + r) + 1)
    ans = 0
    for i in range(t-2, -1, -1):
        fen.update(r[i+1], 1)
        ans += fen.query(l[i]-1)
        # print(fen.fen[:10])
    print(ans)



main()
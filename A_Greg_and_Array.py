from itertools import accumulate
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

    def __init__(self, n):
        self.fenwick= [0]*n
    
    def update(self, pos, val):
        if pos < 1:
            return 
        while pos <= len(self.fenwick):
            self.fenwick[pos-1] += val
            pos += pos & -pos
    
    def querys(self, pos):
        ans = 0
        while pos > 0:
            ans += self.fenwick[pos-1]
            pos -= pos & -pos
        return ans

def main():
    n, m, k = li()
    a = li() + [0]
    Qs = []
    Rs = [0]*(m+1)
    for _ in range(m):
        Qs.append(li())
    for _ in range(k):
        x, y = li()
        Rs[x-1] += 1
        Rs[y] -= 1
    Rs = list(accumulate(Rs))
    fen = Fenwick(n)
    # for i, ai in enumerate(a):
    #     fen.update(i+1, ai)
    b = [0]*(n+1)
    for i in range(len(Qs)):
        l, r, d = Qs[i]
        fen.update(l, d*Rs[i])
        fen.update(r+1, -d*Rs[i])
        # b[l-1] += d*Rs[i]
        # b[r] += -d*Rs[i]
    for i in range(n):
        a[i] += fen.querys(i+1)
    # a = [0]
    # for i in range(n):
    #     a.append(a[-1] + fen.querys(i+1) - fen.querys(i))
    print(*a[:-1])


    



# Set the stack size
threading.stack_size(1 << 27)

# Create and start the main thread
main_thread = threading.Thread(target=main)
main_thread.start()

# Wait for the main thread to complete
main_thread.join()
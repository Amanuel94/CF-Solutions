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
        self.s = ['' for _ in range(n)]
        self.fenwicks = [[0]*n for _ in range(27)]

    
    def _adjust(self, pos, ind, v):
        while pos <= len(self.fenwicks[ind]):
            self.fenwicks[ind][pos-1] += v
            pos += pos & -pos


    def up(self, pos, new):

        old = self.s[pos-1]
        self.s[pos-1] = new
        if old != '':
            oldInd = ord(old) - ord('a')
            self._adjust(pos, oldInd, -1)

        newInd = ord(new) - ord('a')
        self._adjust(pos, newInd, 1)
        # print(new, self.fenwicks[0])
        
    
    def q(self, pos):
        
        cnt = [0]*26
        
        for i in range(26):
            p = pos
            while p > 0:
                cnt[i] += self.fenwicks[i][p-1]
                p -= p & -p
        return cnt

def main():
    s = list(si())
    n = ii()
    fen = Fenwick(len(s))
    for j in range(len(s)):
        fen.up(j+1, s[j])

    for __ in range(n):
        qi = lsi()
        if qi[0] == '1':
            pos, c = int(qi[1]), qi[2]
            fen.up(pos, c)
        else:
            l, r = int(qi[1]), int(qi[2])
            ans = 0
            c = 0
            rl = fen.q(r)
            ll = fen.q(l-1)
            for k in range(26):
                c =  rl[k] - ll[k]
                ans += int(c > 0)
            print(ans)


    

# Set the stack size
threading.stack_size(1 << 27)

# Create and start the main thread
main_thread = threading.Thread(target=main)
main_thread.start()

# Wait for the main thread to complete
main_thread.join()
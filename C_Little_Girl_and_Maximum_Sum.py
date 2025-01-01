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
        self.fenwicks = [[0]*n for _ in range(26)]

    
    def _adjust(self, pos, ind, v):
        while pos <= len(self.fenwicks[ind]):
            self.fenwicks[ind][pos] += v
            pos += pos & -pos


    def up(self, pos, old, new):
        newInd = ord(new) - ord('a')
        oldInd = ord(old) - ord('a')

        self._adjust(pos, newInd, 1)
        self._adjust(pos, oldInd, -1)
    
    def q(self, pos):
        cnt = [0]*26
        p = pos
        for i in range(26):
            ans = 0
            while p > 0:
                ans += self.fenwicks[i][p]
                p -= p & -p
            cnt[i] = ans
        return ans




def main():
    n, q = li()
    a = li()
    Qs = []
    Rs = [0]*(n+1)
    for i in range(q):
        # Qs.append(li())
        l, r = li()
        Rs[l-1] += 1
        Rs[r] -= 1
    Rs = list(accumulate(Rs))[:-1]
    a.sort()
    Rs.sort()
    ans = 0
    for ri, ai in zip(Rs, a):
        ans += ri*ai
    print(ans)
    



# Set the stack size
threading.stack_size(1 << 27)

# Create and start the main thread
main_thread = threading.Thread(target=main)
main_thread.start()

# Wait for the main thread to complete
main_thread.join()
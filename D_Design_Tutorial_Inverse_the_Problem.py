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
    d = []
    p = {i:i for i in range(1, t+1)}
    G = [[] for _ in range(t+1)]
    mb = 20
    anc = [[0]*(mb+2) for _ in range(t+1)]

    def getP(i):
        if i == p[i]:
            return i
        p[i] = getP(p[i])
        return p[i]

    flat = []
    
    for _ in range(t):
        d.append(li())
    for i in range(t):
        if d[i][i] != 0:
            return False
        for j in range(i, t):
            if d[i][j] != d[j][i]:
                return False
            if j > i:
                if d[i][j] == 0:
                    return False
                flat.append((i+1, j+1, d[i][j]))
    flat.sort(key = lambda x: x[-1] )
    for i in range(len(flat)):
        ai, bi, di = flat[i]
        if getP(ai) != getP(bi):
            p[getP(bi)] = p[getP(ai)]
        else:
            lca = getP(ai)
            if d[lca-1][ai-1] + d[lca-1][bi-1] != di:
                return False
    return True

        


            
            
            

        
print(YN(main()))
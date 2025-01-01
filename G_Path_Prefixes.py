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

# def bit_length(x):

#     c = 0
#     while x > 0:
#         x >>= 1
#         c+=1
#     return

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
        G = [[] for _ in range(n+1)]
        bn = 22
        anc = [[0]*(bn + 2) for _ in range(n+1)]
        a = [0]*n
        b = [0]*n
        l = [1]*n
    
        for j in range(2, n+1):
            pj, aj, bj = li()
            anc[j][0] = pj
            G[pj].append(j)
            a[j-1] = aj
            b[j-1] = bj
        # [0, 5, 19, 14, 16, 2, 8, 6, 7] 
        # [0, 6, 17, 16, 17, 1, 9, 4, 7] 
        # [1, 2, 4, 3, 4, 2, 3, 3, 4]
        stack = [1]
        def dfs():
            
            while stack:
                node = stack.pop()
                for nbr in G[node]:
                    a[nbr-1] += a[node-1]
                    b[nbr-1] += b[node-1]
                    l[nbr-1] = l[node-1] + 1
                    stack.append(nbr)
        # dfs(1)
        dfs()
        # print(a, b, l)
        for j in range(1, bn + 1):
            for i in range(1, n+1):
                anc[i][j] =  anc[anc[i][j-1]][j-1]
        r = []

        def kanc(x, k):
            while k > 0:
                b = (k & -k).bit_length() - 1
                x = anc[x][b]
                k -= 1 << b
            return x if x > 0 else 1
      
        r = []
        for i in range(2, n+1):
            d = bs(0, 1<<(bn + 1), lambda x: b[kanc(i, x)-1] <= a[i-1])
            r.append(l[i-1] - d - 1)
        print(*r)
main()
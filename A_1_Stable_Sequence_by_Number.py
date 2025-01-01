
# 1 1
# 1 2
# 2 1 
# 2 2
# 2 3
# 3 2
# 3 3
# 3 4
# 4 3
# 4 4
# 4 5

# 1 1 1 1 1
# 2 3 3 3 3 3 3
# 5  8   9   9 9 9 9
# 13 22 26 27 27 27

# (n, x) => ()

# n, x -> (n - 1, x-1) 

# 1 1 1
# 1 1 2 -- 2
# 1 2 1 -- 3
# 1 2 3
# 2 1 1
# 2 1 2 -- 2
# 2 2 1
# 2 2 3 -- 3
# 2 3 2
# 2 3 4


# 1 1 1  1 1
# 1 1 2  1 2
# 1 2 1  2 1
# 1 2 2  2 2
# 1 2 3  2 3
# 2 1 1  1 1
# 2 1 2  1 2
# 2 2 1  2 1 
# 2 2 2  2 2
# 2 2 3  2 3
# 2 3 2  3 2
# 2 3 3
# 2 3 4
# 3 2 1
# 3 4 5 

# 3 2 1
# 3 2 2
# 3 2 3
# 3 3 2
# 3 3 3
# 3 3 4
# 3 4 3 
# 3 4 4
# 3 4 5


from bisect import bisect_left, bisect_right
from itertools import accumulate
from sys import stdin

input = stdin.readline




# for i in range(100):
#     print(i, rec(6, i))

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
    N = 50
    precomp = [[0]*(N+1) for _ in range(N+1)]
    precomp[1] = [0] + [1]*(len(precomp[1])-1)

    for i in range(2, N+1):
        for j in range(1, N):
            precomp[i][j] = precomp[i-1][j-1] + precomp[i-1][j] + precomp[i-1][j+1]
        precomp[i][N] = precomp[i-1][N-1] + 2*precomp[i-1][N]

    

    def f(n, c):
        if c < len(precomp[n]):
            return precomp[n][c]
        return pow(3, n-1)


    def rec(n, x):
        c = 0
        p = pow(3,n-1)
        while c < len(precomp[n]) and x >= f(n, c):
            x -= f(n, c)
            c+=1
        c += x//p
        ans = [c]
        d = -1
        while n-1:
            if x < f(n-1, c+d):
                n-=1
                c+=d    
                ans.append(c)
                d = -1
            else:
                x -= f(n-1, c+d)
                d+=1
        return ans
                


    n, x = list(map(int, input().split()))
    print(*rec(n, x))

    # for i in range(50):
    #     print(i, rec(3, i))
main()






        

    








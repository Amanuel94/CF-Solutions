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

def pw(n):
    if n & (n-1)!= 0 :
        return 1 << n.bit_length()
    return n

def build(a):
    m = pw(2*len(a))
    tree = [0]*(2*m - 1)

    return tree
    
def update(tree, val, p):
    m = len(tree)//2 + 1
    idx = m - 1 + p
    tree[idx] = val
    while idx:
        idx = (idx - 1)//2
        tree[idx] = tree[2*idx + 1] + tree[idx*2 + 2]

def query(tree, v, tl, tr, l, r):
    if l > r:
        return 0
    if tl == l and tr == r:
        return tree[v]
    tm = (tl + tr)//2
    left = query(tree, 2*v + 1, tl, tm, l, min(tm, r))
    right =  query(tree, 2*v + 2, tm + 1, tr, max(l, tm + 1), r)
    return left + right

def main():
    n = ii()
    a = li()
    prev = [-1]*(n+1)
    ans = [0]*(n)
    sg = build(a)
    for i, x in enumerate(a):
        if prev[x] == -1:
            prev[x] = i
        else:
            ans[x-1] = query(sg, 0, 0, len(sg)//2, prev[x], i)
            # print(x, ans[x-1])
            update(sg, 1, prev[x])
    print(*ans)



# Set the stack size
threading.stack_size(1 << 27)

# Create and start the main thread
main_thread = threading.Thread(target=main)
main_thread.start()

# Wait for the main thread to complete
main_thread.join()
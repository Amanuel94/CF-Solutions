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
    if n & (n-1) != 0:
        return 1 << n.bit_length()
    return n


def build(arr):
    N = len(arr)
    m = pw(N)
    tree = [0]*(2*m - 1)
    for i in range(N):
        tree[m - 1 + i] = arr[i]
    for i in range(m-2, -1, -1):
        tree[i] = min(tree[2*i + 1], tree[2*i + 2])
    
    return tree


def update(tree, pos, val):
    m = (len(tree) + 1)//2
    idx = m - 1 + pos
    tree[0] = min(tree[0], val)
    tree[idx] = val
    # idx = (idx - 1)//2
    while idx:
        idx = (idx - 1)//2
        tree[idx] = min(tree[idx*2 + 1], tree[idx*2 + 2])
    
    # tree[idx] = min(tree[idx*2 + 1], tree[idx*2 + 2])
        


def q(tree, v, tl, tr, l, r):
    if l > r:
        return inf
    if tl == l and tr == r:
        return tree[v]

    tm = (tl + tr)//2
    return min(
        q(tree, 2*v + 1, tl, tm, l , min(tm, r)), 
        q(tree, 2*v + 2, tm+1, tr, max(tm+1, l), r)
    )
    

def query(tree, l, r):
    m = (len(tree) + 1)//2
    return q(tree, 0, 0, m-1, l, r)


def main():
    n, q = li()
    a = li()
    segTree = build(a)
    for _ in range(q):
        t, f, s = li()
        if t == 1:
            update(segTree, f, s)
        else:
            print(query(segTree, f, s-1))


# Set the stack size
threading.stack_size(1 << 27)

# Create and start the main thread
main_thread = threading.Thread(target=main)
main_thread.start()

# Wait for the main thread to complete
main_thread.join()
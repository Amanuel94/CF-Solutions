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
    if n & (n - 1) != 0:
        return 1 << n.bit_length()
    return n

def build(a):
    m = pw(len(a))
    tree = [0]*(2*m - 1)
    for i in range(len(a)):
        tree[m - 1 + i] = a[i]
    
    for i in range(m-2, -1, -1):
        tree[i] = max(tree[2*i + 2], tree[2*i + 1])
    
    return tree

def update(tree, p, val):
    m = len(tree)//2 + 1
    idx = m - 1 + p
    tree[idx] = val
    while idx:
        idx = (idx - 1)//2
        tree[idx] = max(tree[2*idx + 1], tree[2*idx + 2])

def query(tree, x, v, l, tl, tr):

    if tree[v] < x or tr < l:
        return inf
    
    if tl == l:
        while v <= len(tree)//2 - 1:
            if tree[2*v + 1] >= x:
                v = 2*v + 1
            else:
                v = 2*v + 2
        return v - (len(tree)//2)
    
    tm = (tl + tr)//2
    # if tl <= l:
    return min(query(tree, x, 2*v+1, l, tl, tm), 
    query(tree, x, 2*v + 2, tm + 1, tm+1, tr))
    # else:
    #     return min(query(tree, x, 2*v+1, l, tl, tm), query(tree, x, 2*v + 2, tm + 1, tm+1, tr))


def qr(tree, x, v, tl, tr, l, r):
    # print(tl, tr, end="....")
    if tree[v] < x or tr < l:
        return inf
    
    if tl == l and tr == r:
        while v <= len(tree)//2 - 1:
            if tree[2*v + 1] >= x:
                v = 2*v + 1
            else:
                v = 2*v + 2
        return v - (len(tree)//2)
    
    tm = (tl + tr)//2
    left = qr(tree, x, 2*v + 1, tl, tm, l, min(tm, r))
    right = qr(tree, x, 2*v + 2, tm+1, tr, max(l, tm + 1), r)
    # print(lef?t, right, v, tl, tm, tm + 1, tr)
    return min(
        left,
        right
        
    )

      

    

def main():
    n, q = li()
    a = li()
    sg = build(a)
    while q:
        t = li()
        if t[0] == 1:
            update(sg, t[1], t[2])
        else:
            ans = qr(sg, t[1], 0, 0, len(sg)//2, t[2], len(sg)//2)
            print(ans if ans != inf else -1 )
        q-=1
# Set the stack size
threading.stack_size(1 << 27)

# Create and start the main thread
main_thread = threading.Thread(target=main)
main_thread.start()

# Wait for the main thread to complete
main_thread.join()
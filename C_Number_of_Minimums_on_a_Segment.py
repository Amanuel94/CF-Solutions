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
    if n & ( n- 1)!= 0:
        return 1 << n.bit_length()
    return n

def build(a):
    m = pw(len(a))

    tree = [0]*(2*m - 1)
    treemp = [{} for _ in range(2*m - 1)]
    for i in range(len(a)):
        tree[m - 1 + i] = a[i]
        treemp[m - 1 + i][a[i]] = 1

    for i in range(m-2, -1, -1):
        tree[i] = min(tree[2*i + 1], tree[2*i + 2])
        for k in treemp[2*i + 1]:
            treemp[i][k] = treemp[i].get(k, 0) + treemp[2*i + 1][k]

        for k in treemp[2*i + 2]:
            treemp[i][k] = treemp[i].get(k, 0) + treemp[2*i + 2][k]
    
    return tree, treemp

def update(tree, treemp, p, val):
    m = (len(tree)+1)//2
    idx = m -  1 + p
    prev = tree[idx]
    tree[idx] = val
    treemp[idx][prev]-=1
    treemp[idx][val] = 1
    while idx:
        idx = (idx - 1)//2
        tree[idx] = min(tree[2*idx + 1], tree[2*idx + 2])
        treemp[idx][prev] -= 1
        treemp[idx][val] = treemp[idx].get(val, 0) + 1
    # tree[idx] = min(tree[2*idx + 1], tree[2*idx + 2])
    # treemp[idx][prev] -= 1
    # treemp[idx][val] = treemp[idx].get(val, 0) + 1


def q(tree, treemp, v, tl, tr, l, r):
    if l > r:
        return inf, 0
    if tl == l and tr == r:
        mn = tree[v]
        cnt =  treemp[v][mn]
        return mn, cnt

    tm = (tl + tr)//2
    mnl, cntl = q(tree, treemp, 2*v + 1, tl, tm, l, min(r, tm))
    mnr, cntr = q(tree, treemp, 2*v + 2, tm + 1, tr, max(tm+1, l), r)
    if mnl == mnr:
        return mnl, cntl + cntr
    elif mnl < mnr:
        return mnl, cntl
    return mnr, cntr

def query(tree, treemp, l, r):
    m = (len(tree)+1)//2
    return q(tree, treemp, 0, 0, m-1, l, r)

def main():
    n, q = li()
    a = li()
    st, stmp = build(a)
    while q:
        t, f, s = li()
        if t == 1:
            update(st, stmp, f, s)
        else:
            print(*query(st, stmp, f, s-1))
        q-=1

# Set the stack size
threading.stack_size(1 << 27)

# Create and start the main thread
main_thread = threading.Thread(target=main)
main_thread.start()

# Wait for the main thread to complete
main_thread.join()
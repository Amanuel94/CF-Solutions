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
    if (n & (n-1)) != 0:
        return 1 << n.bit_length()
    return n


def build(a):
    m = pw(len(a))
    tree = [(0, 0, 0, 0)] * (2*m - 1)  # Store (tree, pref, suff) as tuples
    for i in range(len(a)):
        tree[m - 1 + i] = (a[i], a[i], a[i], a[i])
    
    for i in range(m-2, -1, -1):
        left, right = tree[2*i + 1], tree[2*i + 2]
        tree_sum = left[0] + right[0]
        pref = max(left[1], left[0] + right[1])
        suff = max(right[2], right[0] + left[2])
        mx_sg_sum = max(left[3], right[3], left[2] + right[1])
        tree[i] = (tree_sum, pref, suff, mx_sg_sum)
    
    return tree

def update(tree, pos, val):
    m = (len(tree) + 1)//2
    idx = m - 1 + pos
    prev = tree[idx][0]
    tree[idx] = (val, val, val, val)
    while idx:
        idx = (idx - 1)//2
        left, right = tree[2*idx + 1], tree[2*idx + 2]
        tree_sum = left[0] + right[0]
        pref = max(left[1], left[0] + right[1])
        suff = max(right[2], right[0] + left[2])
        mx_sg_sum = max(left[3], right[3], left[2] + right[1])
        tree[idx] = (tree_sum, pref, suff, mx_sg_sum)

# def query(tree, v = 0):
#     if v > len(tree)//2 - 1:
#         return tree[v][0]
#     return max(query(tree, 2*v + 1), query(tree, 2*v + 2), tree[2*v + 1][2] + tree[2*v + 2][1])

def query(tree):
    return tree[0][3]
        



def main():
    n, q = li()
    a = li()
    sgtr = build(a)
    for _ in range(q):
        print(max(query(sgtr), 0))
        i, v = li()
        update(sgtr, i, v)
    print(max(query(sgtr), 0))

main()

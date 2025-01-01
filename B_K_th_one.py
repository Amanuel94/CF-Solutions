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
        tree[i] = tree[2*i + 2] + tree[2*i + 1]
    
    return tree

def update(tree, p):
    m = len(tree)//2 + 1
    diff = -1 if tree[m - 1 + p] else 1
    idx = m - 1 + p
    tree[idx] += diff
    while idx:
        idx = (idx - 1)//2
        tree[idx] += diff


def query(tree,  k):
    v = 0
    while v <= len(tree)//2 - 1:
        if tree[2*v + 1] > k:
            v = 2*v + 1
        else:
            v = 2*v + 2
            k = k - tree[v-1]
    return v - (len(tree)//2)



def main():
    n, q = li()
    a = li()
    sg = build(a)
    for _ in range(q):
        t, a = li()
        if t == 1:
            update(sg, a)
        else:
            print(query(sg, a))
    
# Set the stack size
threading.stack_size(1 << 27)

# Create and start the main thread
main_thread = threading.Thread(target=main)
main_thread.start()

# Wait for the main thread to complete
main_thread.join()
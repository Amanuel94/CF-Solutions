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
    n  = int(input())
    

    b = [0]*n
    m = {}
    bi = bj = -1
    ci = cj = -1

    res = [0]*n
    for i in range(1, n):

        print(f"XOR 1 {i+1}")
        print()
        sys.stdout.flush()

        b[i] = ii()
        
        if b[i] in m:
            bi = i
            bj = m[b[i]]

        di = b[i] ^ (n - 1)
        if di in m:
            ci = i
            cj = m[di]

        m[b[i]] = i
    
    if bi != -1:
        print(f"AND {bi + 1} {bj + 1}")
        sys.stdout.flush()
        print()
        x = ii()
        
        b[0] = x ^ b[bi]
    
    else:
        print(f"AND 1 {ci + 1}")
        sys.stdout.flush()
        print()
        x1 = ii()
        
        print(f"AND 1 {cj + 1}")
        sys.stdout.flush()
        print()
        x2 = ii()
        
    
        b[0] = x1 + x2
    
    for i in range(1, n):
            b[i] = b[0] ^ b[i]
    
    print("!", end=" ")
    print(*b)
        




    

    
        

# Set the stack size
threading.stack_size(1 << 27)

# Create and start the main thread
main_thread = threading.Thread(target=main)
main_thread.start()

# Wait for the main thread to complete
main_thread.join()
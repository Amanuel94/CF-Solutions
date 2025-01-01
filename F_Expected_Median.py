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
    
    for _ in range(t):
        n, k = li()
        fact = [1] * (n + 3)
        inv_fact = [1] * (n + 3)

        for i in range(2, (n + 3)):
            fact[i] = fact[i-1] * i % MOD

        inv_fact[n + 2] = pow(fact[n + 2], MOD - 2, MOD)
        for i in range(n + 1, 0, -1):
            inv_fact[i] = inv_fact[i+1] * (i+1) % MOD

        def nCk(n, k):
            if k < 0 or k > n:
                return 0
            return fact[n] * inv_fact[k] % MOD * inv_fact[n-k] % MOD
        
        a = li()
        a.sort()
        ans = 0
        for i in range(n):
            ans += (nCk(i, k//2)*nCk(n-i-1, k//2))%MOD*a[i]
        print(ans%MOD)



# Set the stack size
threading.stack_size(1 << 27)

# Create and start the main thread
main_thread = threading.Thread(target=main)
main_thread.start()

# Wait for the main thread to complete
main_thread.join()
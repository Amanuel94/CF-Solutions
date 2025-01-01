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
        a = si()
        b = si()
        c = si()

        dp = [[inf]*(len(b) + 1) for _ in range(len(a) + 1)]
        dp[len(a)][len(b)] = 0

        for i in range(len(a), -1, -1):
            for j in range(len(b), -1, -1):
                dp[i-1][j] = min(int(a[i-1] != c[i + j-1]) + dp[i][j], dp[i-1][j])
                dp[i][j-1] = min(int(b[j-1] != c[i + j-1]) + dp[i][j], dp[i][j-1])

    
        print(dp[0][0])
        

# Set the stack size
threading.stack_size(1 << 27)

# Create and start the main thread
main_thread = threading.Thread(target=main)
main_thread.start()

# Wait for the main thread to complete
main_thread.join()
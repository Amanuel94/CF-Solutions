import sys, threading
input = sys.stdin.readline
from collections import defaultdict, deque
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
        n = ii()
        G = [[] for _ in range(n)]
        inc = [0]*n
        
        for _ in range(n):
            order = li()
            for i in range(1, n-1):
                G[order[i-1]-1].append(order[i]-1)
                inc[order[i]-1]+=1
        root = -1 
        for i in range(n):
            if inc[i] == 0:
                root = i
        q = deque([root])

        ans = []
        while q:
            x = q.popleft()
            ans.append(x+1)
            for nbr in G[x]:
                inc[nbr] -=1
                if inc[nbr] == 0:
                    q.append(nbr)
        print(*ans)

# Set the stack size
threading.stack_size(1 << 27)

# Create and start the main thread
main_thread = threading.Thread(target=main)
main_thread.start()

# Wait for the main thread to complete
main_thread.join()
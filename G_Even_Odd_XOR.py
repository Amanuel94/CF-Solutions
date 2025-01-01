import sys, threading
input = sys.stdin.readline
from collections import defaultdict
inf = float('inf')
MOD = 10**9 + 7

# 7
# 

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
        e = 0
        o = 0
        ans = []
        for i in range(n-2):
            if i%2:
                o^=(i+1)
            else:
                e^=(i+1)
            ans.append(i+1)
        if n%2:
            e^=(pow(2, (n-1).bit_length()))
            
        else:
            o^=(pow(2, (n-1).bit_length()))
     
        ans.append(pow(2, (n-1).bit_length()))
        if e^o != pow(2, (n-1).bit_length()):
            ans.append(e^o)
        else:
            ans[0] = 0
            ans.append(e^o + 1)
        print(*ans)


# 0000 #0010
# 0011 #1001
# 1000



            

# Set the stack size
threading.stack_size(1 << 27)

# Create and start the main thread
main_thread = threading.Thread(target=main)
main_thread.start()

# Wait for the main thread to complete
main_thread.join()
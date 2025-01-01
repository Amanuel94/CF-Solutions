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
        n = ii()
        ans = []
        pref = []
        su = 0
        s = si()
        for i in range(n):
            if i < n//2:
                if s[i] == "R":
                    su += n - i - 1
                    pref.append(0)
                else:
                    su += i
                    pref.append(n - i - 1 - i)
            elif n%2 == 0 or i > n//2:
                if s[i] == "L":
                    su += i
                    pref.append(0)
                else:
                    su += n - i - 1
                    pref.append(i - n + i + 1)
            else:
                su += i
                pref.append(0)

        # print(pref)
        pref.sort(reverse=True)
        p = 0
        for i in range(n):
            p += pref[i]
            ans.append(su + p)
        print(*ans)





# Set the stack size
threading.stack_size(1 << 27)

# Create and start the main thread
main_thread = threading.Thread(target=main)
main_thread.start()

# Wait for the main thread to complete
main_thread.join() 
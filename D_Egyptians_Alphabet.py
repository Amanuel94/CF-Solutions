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
    n, m = li()
    s1 = li()
    s2 = li()
    c1 = s1.count(0)
    c2 = s2.count(0)
    t = c1 + c2
    e = 0
    ans = 0
    for i in range(n):
        if s1[i]*s2[i] != 0:
            if s1[i] > s2[i]:
                ans += pow(m, e, MOD)*pow(m, t, MOD)
                ans %= MOD
                break
            if s1[i] < s2[i]:
                break
        else:
            if s1[i] != 0:
                t -= 1
                ans += pow(m, e, MOD)*(s1[i] - 1)*pow(m , t, MOD)
                ans %= MOD
                
            if s2[i] != 0:
                t -= 1
                ans += pow(m, e, MOD)*(m - s2[i])* pow(m, t, MOD)
                ans %= MOD
            if s1[i] == s2[i]:
                t -= 2
                ans += pow(m, e, MOD)*(m*m - m)* pow(m - s2[i], t, MOD)//2
                ans %= MOD
                e += 1
    print((ans * pow(pow(m, c1 + c2, MOD), MOD - 2, MOD))%MOD)




            




    
        

# Set the stack size
threading.stack_size(1 << 27)

# Create and start the main thread
main_thread = threading.Thread(target=main)
main_thread.start()

# Wait for the main thread to complete
main_thread.join()
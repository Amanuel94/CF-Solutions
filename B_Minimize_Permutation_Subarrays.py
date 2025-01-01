import sys, threading
input = sys.stdin.readline
from collections import defaultdict
inf = float('inf')
MOD = 10**9 + 7

"""

1 3 2 5 4
1 3 4 5 2
1 4 2 5 3
4 5 6 1 2 3

8 7 6 3 2 1 4 5 9



Keyword arguments:
argument -- description
Return: return_description
"""


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
        a = li()
        
        # i  = a.index(1)
        # j = a.index(2)
        # if i*j != 2:
        #     if i > 0 or i < n:
        #         k = n if j == 0 else 1
        #         print(min(k, i+1), max(i+1, k))
        #     else:
        #         k = n if i == 0 else 1
        #         print(min(j+1, k), max(j+1, k))
        # else:
        #     i = a.index()
        # i = 0
        # j = n-1
        # e = 1
        # t = 1
        # if a[0] == 2:
        #     t = 0
        #     # i+=1
        # while i < j:
        #     if t:
        #         if a[i] == e:
        #             i+=1
        #         else:
        #             break
        #     else:
        #         if a[j] == e:
        #             j-=1
        #         else:
        #             break
        #     e+=1
        #     t = 1-t
        # if i != j:
        #     k = a.index(e)+1
        #     ans = (min(k, i+1), max(k, i+1)) if t else (min(k, j+1), max(k, j+1))
        #     print(*ans)
        #     continue
        # print(i, j)
        if n <= 2:
            print(1, 1)
            continue

        i = a.index(1)
        j = a.index(2) 


        if i != 0 and i != n-1:
            if n%2 == 0:
                if j < n//2:
                    print(i+1, n)
                else:
                    print(1, i+1)
            else:
                if j < n//2:
                    print(i+1, n)
                elif j > n//2:
                    print(1, i+1)
                else:
                    k = a.index(3)
             
                    if k < n//2:
                        print(i+1, n)
                    elif k > n//2:
                        print(1, i+1)
        else:
            if (i+1)*(j+1) != n: 
                if i == 0:
                    print(j+1, n)
                else:
                    print(1, j+1)
            else:
                print(1,1)
        



# Set the stack size
threading.stack_size(1 << 27)

# Create and start the main thread
main_thread = threading.Thread(target=main)
main_thread.start()

# Wait for the main thread to complete
main_thread.join()
# 2 2 1024
# 2 2 2^10
# c = 
import math
import sys, threading
input = sys.stdin.readline
from collections import defaultdict
inf = float('inf')
MOD = 10**9 + 7
# returns the first number where key becomes true for a given delegate type key
def bs(low=1, high=1, key = lambda x: True):

    while low <= high:
        mid = (low + high)//2
        if key(mid):
            high = mid-1
        else:
            low = mid+1
    return low

def check(n, a, b):
    while n%a == 0:
        n//=a
    
    while n%b == 0:
        n//=b
    return n==1

# k a^i b^j

def inv(a, MOD):
    return pow(a, MOD-2, MOD)

def main():
    t = int(input())
    for _ in range(t):
        a, b, l =  list(map(int, input().split()))
       
        fac = set()
        for i in range(20):
            for j in range(20):
                fac.add(pow(a, i)*pow(b, j))
        count = 0
        for k in fac:
            if l%k == 0:
                count +=1
        print(count)
            







# Set the stack size
threading.stack_size(1 << 27)

# Create and start the main thread
main_thread = threading.Thread(target=main)
main_thread.start()

# Wait for the main thread to complete
main_thread.join()

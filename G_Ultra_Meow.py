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

fact = [0]*5001
fact[0] = 1
for i in range(1, len(fact)):
    fact[i] = (fact[i-1]*i)%MOD

def inv(a):
    MOD = 10**9 + 7
    return pow(a, MOD - 2, MOD)

def comb(n, k, MOD):
    return (((fact[n]*inv(fact[k]))%MOD)*inv(fact[n - k]))%MOD

# cur + sub - (cur - sub)
# 1 _ _ _ _ 6 7-> 4
# _ 2 _ _ _ _ 7 -> 4
# _ _ 3 _ _ _ 7-> 4
# _ _ _ 4 _ _ 7-> 3
# _ _ _ _ 5 _ 7-> 3
# _ _ _ _ _ 6 7 8 _ 10


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        byn = [0]*(n+1)
        byn[0] = 1
        for cur in range(1, n+1):
            for sub in range(1, cur+1):
                bef = cur - sub
                k = sub + 1
                if bef < k:
                    byn[sub] += comb(cur, sub-1, MOD)*(cur + k - bef) 
                elif bef > k:

                



    




# Set the stack size
threading.stack_size(1 << 27)

# Create and start the main thread
main_thread = threading.Thread(target=main)
main_thread.start()

# Wait for the main thread to complete
main_thread.join()

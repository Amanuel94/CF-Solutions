# 3  1  4  1  5  9
# 3  4  8  9  ....
# 
from itertools import accumulate
import sys, threading
input = sys.stdin.readline
from collections import defaultdict
inf = float('inf')
MOD = 10**9 + 7
# returns the first number where key becomes true for a given delegate type key
# 0 1 2 3 4 3 2 1
# F F F F T T T T
def bs(low=1, high=1, key = lambda x: True):

    while low <= high:
        mid = (low + high)//2
        if key(mid):
            high = mid-1
        else:
            low = mid+1
    return low

def art(n):
    return (n*(n+1))//2

def helper(x, l, u, pref):
    if x == len(pref)-1:
        return -inf
    return u*(pref[x] - pref[l-1]) - art(pref[x] - pref[l-1]-1)

# 0 10
# 5 10 9 6 8 3 10 7 3
# 

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        nums =  list(map(int, input().split()))
        pref = list(accumulate([0] + nums)) + [inf]
        # print(pref, helper(2, 1, 1, pref))
        q = int(input())
        for __ in range(q):
            l, u = list(map(int, input().split()))
            r = bs(l, len(pref)-1, key = lambda x: helper(x, l, u, pref) >= helper(x+1, l, u, pref))
            if n == 1: r = 1
            
            if helper(r, l, u, pref) < helper(r+1, l, u, pref):
                r+=1
            print(r, end = " ") 
        print()
            




    




# Set the stack size
threading.stack_size(1 << 27)

# Create and start the main thread
main_thread = threading.Thread(target=main)
main_thread.start()

# Wait for the main thread to complete
main_thread.join()


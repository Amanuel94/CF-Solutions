# 6 8 12 15
# 2 4 3 

import sys, threading
input = sys.stdin.readline
from collections import defaultdict
inf = float('inf')
# returns the first number where key becomes true for a given delegate type key
def bs(low=1, high=1, key = lambda x: True):

    while low <= high:
        mid = (low + high)//2
        if key(mid):
            high = mid-1
        else:
            low = mid+1
    return low

def solve(n, a):
    
    nums = [1]*n
    for i in range(1, n):
        cur = a[i] - a[i-1]
        nums[cur-1]-=1
        count= 0 
        
        for ai in nums:
            if ai == 1:
                count +=1
            if count > 1:
                return "NO"
            if ai < 1:
                return "NO"
        return "YES"


def main():
    t = int(input())
    for _ in range(t):

        n = int(input())
        a =  list(map(int, input().split()))
        print(solve(n, a))
        
        
    




# Set the stack size
threading.stack_size(1 << 27)

# Create and start the main thread
main_thread = threading.Thread(target=main)
main_thread.start()

# Wait for the main thread to complete
main_thread.join()

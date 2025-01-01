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

def left(nums, piv, x, l):
    return nums[x] + piv >= l

def right(nums, piv, x, r):
    return nums[x] + piv > r


def main():
    t = int(input())
    for _ in range(t):
        n, l, r =  list(map(int, input().split()))
        a = list(map(int, input().split()))
        a.sort()
        ans = 0
        for i, piv in enumerate(a[:-1]):
            
            le  = bs(i+1, n-1, key = lambda x: left(a, piv, x, l))
            ri  = bs(i+1, n-1, key = lambda x: right(a, piv, x, r))
            # if _ == 0:
            #     print(piv, le, ri) 
            # if le == i:
            #     le += 1
            # if ri == i:
            #     continue      

            ans += ri - le
        
        # for ai in a:
        #     if l <= 2*ai <= r:
        #         ans -=1

        print(ans)
    




# Set the stack size
threading.stack_size(1 << 27)

# Create and start the main thread
main_thread = threading.Thread(target=main)
main_thread.start()

# Wait for the main thread to complete
main_thread.join()

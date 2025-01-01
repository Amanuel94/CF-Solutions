import sys, threading
input = sys.stdin.readline
from collections import Counter, defaultdict
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

import math
def main():
    t = int(input())
    for _ in range(t):
        n, k =  list(map(int, input().split()))
        nums =  list(map(int, input().split()))

        counter = Counter(nums)
        nums.sort()
        count = 1
        for i in range(n-k+1, n):
            if nums[i-1] == nums[i]:
                count+=1
            else: break
            
        # print(nums[n-k], count)
        print(math.comb(counter[nums[n-k]], count)%(10**9 + 7))

    
    




# Set the stack size
threading.stack_size(1 << 27)

# Create and start the main thread
main_thread = threading.Thread(target=main)
main_thread.start()

# Wait for the main thread to complete
main_thread.join()

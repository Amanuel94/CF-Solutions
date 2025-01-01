import sys, threading
input = sys.stdin.readline
from collections import defaultdict
input = sys.stdin.readline
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


def main():
    n, c = list(map(int, input().split()))
    nums =  list(map(int, input().split()))
    s = sum(nums)
    nums*=2

    left = 0
    max_ind = 0
    max_num = n*(c//max(nums)+1)
    cur = 0
    left, right = 0, 0
    cur = 0
    while left < l:
        if right <  n*(c//max(nums)+1) and (left > right or cur < c):
            cur+=nums[right%n]
            right+=1
        else:
            # print(cur, left, right)
            if right - left < max_num and cur >= c:
                max_num = right - left
                max_ind = left
            cur-=nums[left%n]
            left+=1


    print(max_ind+1, max_num)
        
    




# Set the stack size
threading.stack_size(1 << 27)

# Create and start the main thread
main_thread = threading.Thread(target=main)
main_thread.start()

# Wait for the main thread to complete
main_thread.join()

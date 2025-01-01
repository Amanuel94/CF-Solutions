import sys, threading
input = sys.stdin.readline
from collections import defaultdict
input = sys.stdin.readline

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
    n, k = list(map(int, input().split()))
    nums =  list(map(int, input().split()))
    nums.sort()
    if n == 1:
        print(1, nums[0])
        exit(0)
    dp = [0]*n
    left = 0
    max_op = 0
    ans = 0
    val = -1
    for right in range(1, n):
        # print(dp)
        cur_op = (nums[right] - nums[right-1])*(right - left) + dp[right-1]
        while left <= right and cur_op > k:
            cur_op-=(nums[right] - nums[left])
            left+=1
     
        dp[right] = cur_op
        if ans < right - left +1:
            ans =right - left +1
            val = nums[right]
    print(ans, val)
        






# Set the stack size
threading.stack_size(1 << 27)

# Create and start the main thread
main_thread = threading.Thread(target=main)
main_thread.start()

# Wait for the main thread to complete
main_thread.join()

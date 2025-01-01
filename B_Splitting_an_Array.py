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

def helper(ans, nums, k):

    cur = 0
    for num in nums:
        if cur + num > k:
            k-=1
            cur = 0

        if k == 0:
            return False

        cur+=num
    return True
        

def main():
    n, k =  list(map(int, input().split()))
    nums =  list(map(int, input().split()))
    nums.sort()
    return bs(0, sum(nums), lambda x: helper(x, nums, k))

    


    



print(main())

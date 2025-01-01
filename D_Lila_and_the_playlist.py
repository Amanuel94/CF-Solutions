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


def main():
    n, p = list(map(int, input().split()))
    nums =  list(map(int, input().split()))

    s = sum(nums)
    nums+=nums
    r = p%s
    left, right = 0, 0
    s1 = 0
    max_num = inf
    max_ind = -1
    for right in range(2*n):
        s1+=nums[right]
        if s1 >= r:
            if right - left + 1 < max_num:
                max_num =  right - left + 1
                max_ind = left%n
            while left <= right and s1 >= r:
                s1-=nums[left]
                left+=1
                if s1 >= r and right - left + 1 < max_num:
                    max_num = right - left +1
                    max_ind = left % n                  
        
    while left <= right and s1 >= r:
        s1-=nums[left]
        left+=1
        if s1 >= r:
            if right - left + 1 < max_num:
                max_num = right - left +1
                max_ind = left % n

    print(max_ind+1, max_num + n*(p//s))
        



main()

        

        
                        
    

        
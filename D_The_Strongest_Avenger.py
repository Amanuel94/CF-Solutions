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
    t = int(input())
    for _ in range(t):
        n = int(input())
        nums =  list(map(int, list(input().strip())))
        
        left = right =  0
        sum_ = 0
        count = 0
        while right < n:
            sum_+=nums[right]
            if sum_ == right - left+1:
                left = right+1
                right+=1
                count+=1

            else:
                right+=1
        while left < n:
            sum_-=nums[left]
            left+=1
            if sum_ == right - left+1:
                count+=1
            

            
            
        print(count*(count+1)//2)

main()
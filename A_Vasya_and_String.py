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
    n, k  =  list(map(int, input().split()))
    s = input().strip()
    i = 0
    hash_map = {'a':0, "b":0}
    cur = 0
    left = 0
    max_ = 0
    for right in range(n):
        
        hash_map[s[right]]+=1
        while left < right and min(hash_map['a'] , hash_map['b'])> k:
            hash_map[s[left]]-=1
            left+=1

        max_ = max(max_, right-left+1)
    print(max_)

        




    




main()
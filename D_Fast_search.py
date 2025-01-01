import sys, threading
input = sys.stdin.readline
from collections import defaultdict
inf = float('inf')
# returns the first number where key becomes true for a given delegate type key
# a b c d e
def bs(low=1, high=1, key = lambda x: True):

    while low < high:
        mid = (low + high)//2
        if key(mid):
            high = mid
        else:
            low = mid+1
    return low


def main():
    n = int(input())
    nums =  list(map(int, input().split()))
    nums.sort()
    q = int(input())
    for _ in range(q):

        # low = 0
        # high = len(nums)-1
        # while low < high:

        #     mid = (low + high) // 2
        #     if nums[mid] < q[_]:
        #         low = mid+1
        #     else:
        #         high = mid



        l, r = list(map(int, input().split()))
        # for i in range(len(nums)-1):
        #     print((lambda x: nums[x] < l)(i), end = " ->")
        lans = bs(low = 0, high = len(nums), key = lambda x: nums[x] >= l)
        rans = bs(low = 0, high = len(nums), key = lambda x: nums[x] > r)
        # print(lans, rans)
        print(rans - lans, end =" ")
    print()

main()






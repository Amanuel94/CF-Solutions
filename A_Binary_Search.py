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
    n, k = list(map(int, input().split()))
    nums =  list(map(int, input().split()))
    q = list(map(int, input().split()))
    for _ in range(k):

        # low = 0
        # high = len(nums)-1
        # while low < high:

        #     mid = (low + high) // 2
        #     if nums[mid] < q[_]:
        #         low = mid+1
        #     else:
        #         high = mid
        ans = bs(low = 0, high = len(nums)-1, key = lambda x: nums[x] >= q[_])
        # print(ans)
        print("YES") if ans < len(nums) and nums[ans] == q[_] else print("NO")

main()






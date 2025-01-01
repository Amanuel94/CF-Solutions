import sys
from heapq import heapify, heappop, heappush
input = sys.stdin.readline
# from collections import defaultdict
t = int(input())
for _ in range(t):
    n = int(input())
    nums1 = list(map(int, input().split()))
    # nums = [(int(input))]
    nums = [(-a, r) for r, a in enumerate(nums1) if a != 0]
    # nums2 = [(-a, r) for r, a in enumerate(nums1)]
    heapify(nums)
    # heapify(nums2)
    # print(nums)
    # nums.sort()
    i = len(nums)
    ans = []
    x = y  = None
    while len(nums) >1:
        # print(nums, nums2)
        # print(num s)
        y = heappop(nums)
        x = heappop(nums)
        ans.append([x[1]+1, y[1]+1])
        if y[0] and -y[0]-1:
            heappush(nums, (y[0]+1, y[1]))
        if x[0] and -x[0]-1:
            heappush(nums, (x[0]+1, x[1]))

        

        

    # print(nums, i)
    print(len(ans))
    for i in ans:
        print(*sorted(i))




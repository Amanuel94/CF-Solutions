import sys
import math
input =  sys.stdin.readline
t = int(input())



for _ in range(t):

    n =  int(input())
    nums = list(map(int, input().split()))

    pow = ans = 0

    for i in range(len(nums)):

        while nums[i]&1 ==  0:
            pow+=1
            nums[i]//=2
        ans+=nums[i]
    nums.sort(reverse=True)
    print(int((ans-nums[0]) + nums[0]*math.pow(2, pow)))



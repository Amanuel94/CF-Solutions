from collections import defaultdict
import math

n =  int(input())
nums = defaultdict(int)
for _ in  range(n):
    k = 0
    for c in input():
        i = ord(c) - 97
        k^=(1<<i)

    nums[k]+=1
ans  = 0
for key in nums:
    ans += math.comb(nums[key], 2)

    for power in range(26):

        if (1<<power)^ key in nums:
            ans+= nums[key]*nums[(1<<power)^ key]/2

            

print(int(ans))



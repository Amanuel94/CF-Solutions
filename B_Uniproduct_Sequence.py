n = int(input())
nums = list(map(int, input().split()))

nums.sort()

i = 0
ans = 0
while i < len(nums):
    if nums[i] > 0:
        ans+=nums[i]-1
    elif i < len(nums)-1 and nums[i] < 0 and nums[i+1] <= 0:
        ans+= abs(-nums[i]- 1)
        i+=1
        ans+=abs(-nums[i]-1)

    else:
        ans+=-nums[i]+1
    i+=1
print(ans)
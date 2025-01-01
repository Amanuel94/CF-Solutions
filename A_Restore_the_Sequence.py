t  = int(input())

for _ in range(t):
    n =  int(input())
    nums = list(map(int, input().split()))

    if n == 1:
        print(nums[0])
    else:
        l = 0
        r = n-1
        ans = []
        while l < r:
            ans.append(nums[l])
            ans.append(nums[r])
            l+=1
            r-=1
        if l == r:
            ans.append(nums[l])
        print(*ans)

    
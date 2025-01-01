t =  int(input())

for _ in range(t):
    n  = int(input())
    nums = sorted(list(map(int, input().split())))

    l = 0
    r = len(nums)-1
    area = nums[l]*nums[r]
    while l < r:

        if nums[l] != nums[l+1] or  nums[r] != nums[r-1]:
            print('NO')
            break
        elif nums[l]*nums[r] != area:
            print('NO')
            break
        l+=2
        r-=2
    if l >= r:
        print('YES')





    
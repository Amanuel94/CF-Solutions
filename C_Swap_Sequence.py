n =  int(input())

nums =  list(map(int, input().split()))

i = 0
m = 0
swaps = []
while i < len(nums)-1:
    j = i+1
    cur_min = i
    while j < len(nums):
        if nums[cur_min] > nums[j]:
            cur_min =  j
        j+=1
    if cur_min > i:
        nums[cur_min], nums[i]= nums[i], nums[cur_min]
        swaps.append([i , cur_min])
        m+=1

    i+=1
print(m)
for swap in swaps:
    print(*swap)


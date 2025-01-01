import sys
input =  sys.stdin.readline
n  = int(input())

def tri(a, nums):
    return nums[nums[nums[a]-1]-1] == a+1

nums = list(map(int, input().split()))

f  = 1
for i in range(n):
    if tri(i, nums):
        print('YES')
        f = 0
        break
if f:
    print('NO')


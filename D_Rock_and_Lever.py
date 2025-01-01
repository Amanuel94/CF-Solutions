from collections import defaultdict
t =  int(input())

for _ in range(t):
    n = int(input())
    d = defaultdict(int)
    nums = list(map(int, input().split()))

    for i in nums:
        d[i.bit_length()]+=1

    ans = 0
    for key in d:
        pairs = d[key]*(d[key]-1)//2
        ans+=pairs
    # print(d)
    print(ans)

                
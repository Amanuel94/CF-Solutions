import math
t =  int(input())

for _ in range(t):
    n = int(input())
    nums =  list(map(int, input().split()))
    
    cage = 0
    pigs = 0
    unk = 0
    
    for num in nums:

        if num == 1:
            pigs+=1
            unk+=1
        else:
            cage += max(unk, 0)
            if pigs:
                temp =  -cage + (math.ceil((pigs+1)/2))
            else:
                temp = 0

            unk = temp
        # print(unk)
    cage+=max(unk, 0)
    print(cage)
        
        


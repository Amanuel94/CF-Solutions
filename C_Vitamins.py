# from collections import defaultdict
n = int(input())
juices = []
dp = [[float('inf')]*8 for i in range(n+1)]
dp[0][0] = 0
for i in range(1, n+1):
    price, vits = input().split()
    bit = 0
    for vit in vits:
        bit|=1<<((ord(vit)-ord('A')))
    for j in range(8):
        dp[i][j] = min(dp[i-1][j], int(price) + dp[i-1][~bit & j])
if dp[-1][7] == float('inf'):
    print(-1)
else:
    print(dp[-1][7])





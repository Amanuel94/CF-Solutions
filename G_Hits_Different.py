from collections import defaultdict
t = int(input())
dp = [0]*(3*10**6)
dp[1] = 1
memo = defaultdict(int)
def toNum(i, j):
    if j <= 0 or j > i:
        return 0
    return j + i*(i-1)//2

for i in range(2, 2024):
    for j in range(1,i+1):
        dp[toNum(i, j)] = dp[toNum(i-1, j)] + dp[toNum(i-1, j+1)] + toNum(i,j)**2

        
def getRow(n):
    i = 1
    while n-i > 0:
        n-=i
        i+=1
    return i


for _ in range(t):
    n = int(input())
    row = getRow(n)
    col = n - row*(row+1)//2
    print(dp[toNum(row,)])

    
    

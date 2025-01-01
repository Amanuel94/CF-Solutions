import sys
from collections import defaultdict

MOD = 1000000007
N = 40004

def main():
    input = sys.stdin.readline
    pals = []
    for i in range(1, 2 * N):
        if str(i) == str(i)[::-1]:
            pals.append(i)
    
    dp = [[0] * N for _ in range(len(pals) + 1)]
    
    for i in range(len(pals) + 1):
        dp[i][0] = 1
        
    for cur in range(1, N):
        for i in range(len(pals) - 1, -1, -1):
            if pals[i] <= cur:
                dp[i][cur] += dp[i][cur - pals[i]] % MOD
            dp[i][cur] += dp[i + 1][cur] % MOD
    
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(dp[0][n] % MOD)

if __name__ == "__main__":
    main()

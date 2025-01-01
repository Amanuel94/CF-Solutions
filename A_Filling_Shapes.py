import sys, threading
input = sys.stdin.readline
from collections import defaultdict

def main():
    n = int(input())

    dp = [0]*(max(n+1, 3))

    dp[2] = 2



    for i in range(3, n+1):
        dp[i] = 2*dp[i-2]

    return dp[n]



    
    
    




print(main())

import sys, threading
input = sys.stdin.readline
from collections import defaultdict
input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        nums =  list(map(int, input().split()))
        s = min(nums)
        ans = 0
        for num in nums:
            ans+= (num - s)
        print(ans)
    

main()
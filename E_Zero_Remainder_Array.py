import sys, threading
input = sys.stdin.readline
from collections import Counter
input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        n, k =  list(map(int, input().split()))
        nums =  list(map(int, input().split()))
        nums = [num%k for num in nums if num%k > 0]
        c = sorted(Counter(nums).items(), key = lambda k: (k[1], -k[0]))
        # print(c)
        if len(c) == 0:
            print(0)
        else:
            r = (-c[-1][0])%k
            print((c[-1][-1]-1)*k + r+1)
            
main()
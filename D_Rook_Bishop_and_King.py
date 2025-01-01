
import sys, threading
input = sys.stdin.readline
from collections import defaultdict
input = sys.stdin.readline

def main():
    r1, c1, r2, c2 =  list(map(int, input().split()))

    R = 0
    B = 0
    K = 0

    if r1  == r2 or c1 == c2:
        R = 1
    else:
        R = 2
    
    if (r1 + c1)%2 == (r2 + c2)%2:
        if r1 + c1 == r2 + c2 or r1 - c1 == r2 - c2:
            B = 1
        else:
            B = 2
    K = max(abs(r2 - r1), abs(c2 -c1))
    print(R, B, K)

    




main()

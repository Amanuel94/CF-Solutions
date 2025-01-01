import sys, threading
input = sys.stdin.readline
from collections import defaultdict
inf = float('inf')
MOD = 10**9 + 7

def main():
    t = int(input())
    for _ in range(t):
        s  =  input().strip()
        upper = []
        lower = []
        for i, si in enumerate(s):
            if si.upper() != "B":
                if si.upper() == si:
                    upper.append((i,si))
                else:
                    lower.append((i, si))
            else:
                if si.upper() == si and upper:
                    upper.pop()
                elif si.lower() == si and lower:
                    lower.pop()
            # print(si, upper, lower)
        print("".join([u[1] for u in sorted(upper + lower)]))
main()
    

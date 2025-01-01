import sys
input = sys.stdin.readline
T = int(input())
for i in range(T):
    l, r = list(map(int, input().split()))
    print(*[l, 2*l])
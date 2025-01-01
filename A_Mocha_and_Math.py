import sys
input = sys.stdin.readline
t = int(input())
# nums =  list(map(int, input().split()))
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    ans = a[0]
    for i in a:
        ans&=i
    print(ans)

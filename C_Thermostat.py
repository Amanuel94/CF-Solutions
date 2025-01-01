def solve():
    l, r, x = map(int, input().split())
    a, b = map(int, input().split())
    if a == b:
        return 0
    if abs(a - b) >= x:
        return 1
    if r - max(a, b) >= x or min(a, b) - l >= x:
        return 2
    if r - b >= x and a - l >= x or r - a >= x and b - l >= x:
        return 3
    return -1


t = int(input())
for _ in range(t):
    print(solve())
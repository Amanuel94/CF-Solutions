import sys
input = sys.stdin.readline
from collections import defaultdict
def getP(a, p):
    if a == p[a]:
        return a
    p[a] = getP(p[a], p)
    return p[a]

def unite(a, b, p, rk):
    a = getP(a, p)
    b = getP(b, p)
    if a == b:
        return
    if rk[a] < rk[b]:
        a, b = b, a
    p[b] = a
    rk[a] += rk[b]

n, m = map(int, input().split())
p = [i for i in range(n)]
rk = [1] * n

for _ in range(m):
    k, *nodes = map(int, input().split())
    lst = -1
    for x in nodes:
        x -= 1
        if lst != -1:
            unite(x, lst, p, rk)
        lst = x

output = " ".join(str(rk[getP(i, p)]) for i in range(n))
print(output)

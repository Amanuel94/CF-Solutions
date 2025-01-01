import sys
input = sys.stdin.readline
from collections import defaultdict, deque
n, m = list(map(int, input().split()))


xp  = {i:0 for i in range(1, n+1)}
off = {i:0 for i in range(1, n+1)}
p = {i:i for i in range(1, n+1)}


def getP(i):
    if i == p[i]:
        return i
    p[i] = getP(p[i])
    return p[i]

for _ in range(m):
    op, *num = input().split()
    if op == "join":
        X, Y = num
        X, Y = int(X), int(Y)
        X, Y = min(X,Y), max(X,Y)
        for i in range(1, n+1):
            if getP(i) == getP(Y):
                off[i]-=xp[getP(X)]
        p[getP(Y)] = getP(X)

    elif op == "add":
        X, Y = num
        X, Y = int(X), int(Y)
        xp[getP(X)] += Y
    else:
        X = int(num[0])
        print(xp[getP(X)] + off[X])


    


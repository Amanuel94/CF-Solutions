import sys, threading
input = sys.stdin.readline
from collections import defaultdict
input = sys.stdin.readline
from bisect import bisect_left, bisect_right
def main():
    n = int(input())
    q = list(map(int, input().split()))
    m = int(input())
    G = defaultdict(list)
    edges = []
    for i in range(m):
        a, b, c = list(map(int, input().split()))
        edges.append([a,b,c])
    edges.sort(key = lambda x:x[-1])
    # print(edges)
    p = {i:i for i in range(1, n+1)}
    def getP(i):
        if i == p[i]:
            return i
        p[i] = getP(p[i])
        return p[i]
    
    cost = 0
    for a, b,c in edges:
        # print(p,  getP(a), getP(b))
        if getP(a) != getP(b) and q[a-1] > q[b-1] and getP(b) == b:
            # G[a].append(b)
            # G[b].append(a)
            
            p[b] = getP(a)
            cost+=c
    for i in range(1, n+1):
        x = getP(i)

    if len(set(p.values())) > 1:
        print(-1)
    else:
        print(cost)
main()
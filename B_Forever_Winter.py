import sys
input = sys.stdin.readline
from collections import defaultdict, deque

t = int(input())
for _ in range(t):
    n,  m  = list(map(int, input().split()))
    inc = [0]*n
    G = defaultdict(list)
    for j in range(m):
        u, v = list(map(int, input().split()))
        G[u].append(v)
        G[v].append(u)
        inc[u-1]+=1
        inc[v-1]+=1

    # q = deque([i+1 for i in range(n) if inc[i] == 1])
    # vis = set([i+1 for i in range(n) if inc[i] == 1])
    # xy  = []
    # while q:
    #     y_p  = len(q)
    #     # print(q)
    #     xy.append(y_p)
    #     if len(xy) == 2:
    #         break
    #     for _ in range(y_p):
    #         x = q.popleft()

    #         for nbr in G[x]:
    #             if nbr not in vis:
    #                 inc[nbr-1]-=1
    #                 if inc[nbr-1]==1:
    #                     q.append(nbr)
    #                     vis.add(nbr)

    xy = len([i+1 for i in range(n) if inc[i] == 1])
    x = n - xy - 1

    print(x, end = " ")
    print(xy//x)






        

import sys
input = sys.stdin.readline
from collections import deque

n, m =  list(map(int, input().split()))
G = [[] for i in range(n)]
inc = [0]*n

for _ in range(m):
    u, v =  list(map(int, input().split()))
    G[u-1].append(v-1)
    G[v-1].append(u-1)
    inc[v-1]+=1
    inc[u-1]+=1
q=  deque([i for i in range(n) if inc[i]==1])
vis = set()
ans = 0
while q:  
    # print(inc)  
    ans+=1
    batch = len(q)
    stack  = []
    for _ in range(batch):
        x = q.popleft()
        stack.append(x)
        for nbr in G[x]:
            inc[nbr]-=1
    while stack:
        x = stack.pop()
        for nbr in G[x]:
            if  nbr not in vis and inc[nbr] == 1:
                q.append(nbr)
                vis.add(nbr)
print(ans)


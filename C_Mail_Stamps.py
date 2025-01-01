import sys
input = sys.stdin.readline
from collections import defaultdict

n = int(input())
graph =  defaultdict(list)
start = 0
for _ in range(n):
    u, v =  list(map(int, input().split()))
    graph[u].append(v)
    graph[v].append(u)
    
for v in graph:
    if len(graph[v]) == 1:
        start = v
ans = []
i = 0
vis = set()
while i < n+1:
    vis.add(start)
    ans.append(start)
    for nbr in graph[start]:
        if nbr not in vis:
            start = nbr
            break
    i+=1
print(*ans)


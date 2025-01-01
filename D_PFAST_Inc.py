import sys
input = sys.stdin.readline
from collections import defaultdict
n, m = list(map(int, list(input().split())))
graph = defaultdict(list)
vis = set()
g = []
for _ in range(n):
    x = input()
    if x[-1] == '\n':
        x = x[:-1]
    graph[x]= []
    

for _ in range(m):
    u, v = input().split()
    graph[u].append(v)
    graph[v].append(u)
# print(graph)
def dfs(node):
    vis.add(node)
    for nbr in graph[node]:
        if nbr not in vis:
            dfs(nbr)

for p in graph:
    if p not in vis:
        dfs(p)
        g.append(p)
print(len(g))
g.sort()
for a in g:
    print(a)



    
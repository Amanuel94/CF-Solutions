import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
graph = defaultdict(list)
for i in range(1, n+1):
    boss = int(input())
    if boss != -1:
        graph[boss].append(i)

def dfs(node, visited,  depth):
    visited.add(node)
    max_depth = depth
    for nbr in graph[node]:
        if nbr not in visited:
            max_depth = max(max_depth, dfs(nbr, visited, depth+1))
    return max_depth

ans = 1
vis  =set()
for i in range(1, n+1):
    if i not in vis:
        ans = max(ans, dfs(i, vis, 1))

print(ans)

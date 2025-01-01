import sys
input = sys.stdin.readline
from collections import defaultdict, deque

sys.setrecursionlimit(10**6)

graph = defaultdict(list)

n, m = list(map(int, input().split()))
a  = list(map(int, input().split()))

for i in range(m):
    u,v = list(map(int, input().split()))
    graph[v].append(u)
    graph[u].append(v)

vis = set()
def dfs(node):
    ans = a[node-1]
    vis.add(node)
    for nbr in graph[node]:
        if nbr not in vis:
            ans = min(ans, dfs(nbr))
    return ans
        

def bfs(node):
    q = deque([node])
    ans = a[node-1]
    while q:
        cur = q.popleft()
        ans = min(ans, a[cur-1])
        for nbr in graph[cur]:
            if nbr not in vis:
                q.append(nbr)
                vis.add(nbr)
    return ans


res = 0
for node in range(n):
    if node+1 not in vis:
        res+=(bfs(node+1))
print(res)

        
        
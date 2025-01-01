import sys
input = sys.stdin.readline
from collections import defaultdict, deque 

sys.setrecursionlimit(10**5)



V, E = list(map(int, input().split()))

G = [[] for _ in range(V)]
for _ in range(E):
    u, v = list(map(int, input().split()))
    G[u-1].append(v)
    G[v-1].append(u)
B = set()
R = set()
colors = [B, R]

def bfs(node, t, vis):
    q =deque([node])
    vis.add(node)
    while q:

        lvl = len(q)
        t = 1 - t
        for _ in range(lvl):
            x = q.popleft()
            colors[t].add(x)
            for nbr in G[x-1]:
                if nbr in colors[t]:
                    return False
                if nbr not in vis and nbr not in colors[1-t]:
                    q.append(nbr)
                    vis.add(nbr)
    return True

vis = set()
for node in range(1, V+1):
    if node not in vis:
        if not bfs(node, 1, vis):
            print(-1)
            break
else:
    print(len(B))
    print(*B)
    print(len(R))
    print(*R) 

# print(colors)
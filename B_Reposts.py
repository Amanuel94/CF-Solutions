import sys
from collections import defaultdict
graph = defaultdict(list)
input = sys.stdin.readline
n = int(input())
for _ in range(n):
    u, v =  input().split(' reposted ')
    graph[u.lower()].append(v.lower())
    graph[v.lower()].append(u.lower())
# print(graph['polycarp\n'])
# print(graph)
    
# print(graph)
def dfs(node, depth, vis):
    # print(node, graph[node])
    vis.add(node)
    max_depth = depth
    for nbr in graph[node]:
        if nbr+'\n' in graph and nbr+'\n' not in vis:
            max_depth = max(max_depth, dfs(nbr+'\n', depth+1, vis))
        if nbr in graph and nbr not in vis:
            max_depth = max(max_depth, dfs(nbr, depth+1, vis))
    return max_depth
if 'polycarp\n' in graph:
   print(dfs('polycarp\n', 1, set()))
else:
    print(dfs('polycarp', 1, set()))


    
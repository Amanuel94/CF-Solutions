import sys
input = sys.stdin.readline
from collections import defaultdict, deque

n, t = list(map(int, input().split()))
a = list(map(int, input().split()))

graph = defaultdict(list)
for i, ai in enumerate(a):
    graph[i+1].append(i+1+ai)

q = deque([1])
v = set([1])
f = 1
while q:
    x = q.popleft()
    if x == t:
        print("YES")
        f = 0
        break
    for nbr in graph[x]:
        if nbr not in v:
            q.append(nbr)
            v.add(nbr)
if f:
    print("NO")
    



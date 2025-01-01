from collections import defaultdict, deque

def bfs1(start, adj, s, target):
    queue = deque([(start, 0)])
    while queue:
        u, x = queue.popleft()
        if u == target:
            continue
        s.add(x)
        for v, w in adj[u]:
            if v not in s:
                queue.append((v, x ^ w))

def bfs2(start, adj, s, target):
    queue = deque([(start, 0)])
    visited = set()
    while queue:
        u, x = queue.popleft()
        if u != target and x in s:
            return True
        visited.add(u)
        for v, w in adj[u]:
            if v not in visited:
                queue.append((v, x ^ w))
                visited.add(v)
    return False

def solve():
    s = set()
    n, a, b = map(int, input().split())
    a -= 1
    b -= 1
    adj = defaultdict(list)
    for _ in range(n - 1):
        u, v, w = map(int, input().split())
        u -= 1
        v -= 1
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    bfs1(a, adj, s, b)
    if bfs2(b, adj, s, b):
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()

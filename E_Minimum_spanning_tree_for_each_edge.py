import sys, threading
input = sys.stdin.readline
from collections import defaultdict
inf = float('inf')
MOD = 10**9 + 7

def si():
    return input().strip()
def ii():
    return int(input())
def lsi():
    return input().strip().split()
def mi():
    return map(int, input().split())
def li():
    return list(map(int, input().split()))

def main():
    n, m = li()
    edges =  []
    qs = []
    # mst_edges = set()


    for i in range(m):
        u, v, w = li()
        edges.append((i, u, v, w))
        qs.append(edges[-1])
    edges.sort(key= lambda x: x[-1])

    p = {i:i for i in range(1, n+1)}
    def getP(x):
        t = x
        while x != p[x]:
            x = p[x]
        while p[t] != x:
            p[t], t = x, p[t]
        return x

    
    mst = [[] for _ in range(n+1)]
    mb = 20
    up = [[0]*(mb+2) for _ in range(n+1)]
    mx = [[-inf]*(mb+2) for _ in range(n+1)]
    count  = 0
    mw = 0
    r = 0
    for i, u, v, w in edges:
        if getP(u) != getP(v):
            u, v = min(u, v), max(u, v)
            mst[u].append((v, w))
            mst[v].append((u, w))
            mw += w
            p[getP(u)] = getP(v)
            count += 1
        if count == n - 1:
            break
    lvl = [0] * (n + 1)
    strt = [0] * (n + 1)
    en = [0] * (n + 1)

    def dfs(node, time):
        for nbr, wgt in mst[node]:
            if lvl[nbr] == 0:
                time += 1
                lvl[nbr] = lvl[node] + 1
                up[nbr][0] = node
                mx[nbr][0] = wgt
                strt[nbr] = time
                time = dfs(nbr, time)
        time += 1
        en[node] = time
        return time

    lvl[1] = 1
    strt[1] = 1
    dfs(1, 1)


    def is_ancestor(u, v):
        return strt[u] <= strt[v] and en[u] >= en[v]
    
    for j in range(1, mb):
        for i in range(2, n+1):
            up[i][j] = up[up[i][j-1]][j-1]
            mx[i][j] = max(mx[i][j-1], mx[up[i][j-1]][j-1])
    

    def ancestor(u, k):
        m = -inf
        while k > 0:
            b = ((k&-k).bit_length())-1
            m = max(m, mx[u][b])
            u = up[u][b]
            k -= (1 << b)
        return max(u, 1), m

    
    

    def LCA(u, v):
        
        if is_ancestor(u, v): return u
        if is_ancestor(v, u): return v

        for i in range(mb, -1, -1):
            fu, _ = ancestor(u, 1 << i)
            if not is_ancestor(fu, v) :
                u =  fu
        
        return ancestor(u, 1)[0]

    
    # print(LCA(4, 6))
    # print(mst)
    # edges.sort()
    ans = []
    for i, u, v, w in qs:
        # if (min(u, v), max(u, v))  in mst_edges:
        #     ans.append(mw)
        #     continue

        lca = LCA(u, v)
        ld = lvl[u] - lvl[lca]
        _, mia = ancestor(u, ld)
        ld = lvl[v] - lvl[lca]
        _, mib = ancestor(v, ld)
        # b, mib = trace(v, lca)
        ans.append(mw + (w - max(mia, mib)))
    print("\n".join(map(str, ans)))
    
main()
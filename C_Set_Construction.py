import sys
input = sys.stdin.readline
from collections import defaultdict
t = int(input())

for _ in range(t):
    d = defaultdict(set)
    roots = []
    
    n =  int(input())
    par = [-1]*n
    for i in range(n):
        isRoot = 1
        for j, c in enumerate(input()):
            # print(par)
            if c =='1':
                if par[i]+1 not in d[j+1]:
                    d[j+1].add(i+1)
                elif par[i] == par[j]:
                    d[par[i]+1].discard(i+1)
                par[i] = j 
                isRoot = 0
            

        if isRoot:
            roots.append(i+1)

    

    print(d)
    ans = [False for _ in range(n)]
    def dfs(node, vis):
        # vis.add(node)
        ans[node-1] = set([node])
        for nbr in d[node]:
            # if nbr not in vis:
            ans[node-1] = ans[node-1] | dfs(nbr, vis)
        # ans[node-1] = sub
        return ans[node-1]

    for root in roots:
        dfs(root, set())
    for key in ans:
        print(len(key), end = ' ')
        print(*(key))

        


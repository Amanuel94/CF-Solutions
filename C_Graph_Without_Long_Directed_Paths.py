import sys
from heapq import heapify, heappop, heappush
input = sys.stdin.readline
from collections import defaultdict
n, m = list(map(int, list(input().split())))
edges = []
for _ in range(m):
    edges.append(list(map(int, input().split())))
# graph = defaultdict(list)
# col = defaultdict(int)
# vis = set()

# for


# def dfs(node):
#     col[node] = 1
#     ans = True
#     vis.add(node)
#     for nbr in graph[node]:
#         if nbr not in vis and col[nbr] == 0:
#             ans = ans and dfs(nbr)
#         elif col[nbr] == 1:
#             return False
#     return ans

# for _ in range(m):
#     if dfs(0):

#     else:
#         print('NO'
ans = []
def func():
    inc = set()
    out = set()
    # out = set()
    
    for u, v in edges:
        # if (u in inc and v in inc) or (u in out and v in out):
        #     return False
        # if u in inc and v not in inc and u not in out:
        #     # inc.add(u)
        #     ans.append(1)
        #     out.add(v)
        # elif v in inc and u not in inc and v not in out:
        #     ans.append(0)
        #     out.add(u)
        # elif u not in out:
        #     inc.add(u)
        #     ans.append(1)
        #     out.add(v)
        # elif v not in out:
        #     inc.add(v)
        #     ans.append(0)
        #     out.add(u)

        if u in inc:
            if v in inc:
                return False
            else:
                ans.append(1)
                out.add(v)

        elif u in out:
            if v in out:
                return False
            else:
                ans.append(0)
                inc.add(v)
        else:
            if v in inc:
                ans.append(0)
                out.add(u)
            elif v in out:
                ans.append(1)
                inc.add(u)
            else:
                ans.append(1)
                inc.add(u)
                out.add(v)


    return True
        

            

    return True
if func():
    print("YES")
    print("".join(list(map(str, ans))))
else:
    print("NO")



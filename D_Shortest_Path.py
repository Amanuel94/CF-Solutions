import sys, threading
input = sys.stdin.readline
from collections import defaultdict,deque
input = sys.stdin.readline

def main():
    n, m,k = list(map(int, input().split()))
    G = defaultdict(list)
    for _ in range(m):
        x, y = list(map(int, input().split()))
        G[x].append(y)
        G[y].append(x)
    forbidden = set()
    for i in range(k):
        forbidden.add(tuple(map(int, input().split())))
        
    # q = deque([[1, [0,1], [1]]])
    # # print(q)
    # vis = set((1, (0,1)))
    # while q:
    #     # print(q)
    #     x, cur, ans = q.popleft()
    #     # ans = ans[:]
        
    #     for nbr in G[x]:
    #         s = cur[:]
    #         if len(s) < 3:
    #             s.append(nbr)
    #         else:
    #             s = s[1:] + [nbr]
    #         if (nbr, tuple(s)) not in vis and tuple(s) not in forbidden:
    #             # ans.append(nbr)
    #             q.append([nbr, s, ans + [nbr]])
    #             vis.add((nbr, tuple(s)))
                
                
    #             if nbr == n:
    #                 print(len(ans))
    #                 print(*(ans+[nbr]))
    #                 exit()
    # print(-1)
    g_ans = []
    g_len = float('inf')
    vis = defaultdict(int)
    def dfs(node, prev, ans):
        nonlocal g_len
        nonlocal g_ans
        vis[node]=1
        ans.append(node)
        if node == n:
            if g_len > len(ans):
                g_ans = ans[:]
                g_len = len(ans)
                
        else:
            for nbr in G[node]:
                if nbr != 1 and  (prev, node,  nbr) not in forbidden:
                    dfs(nbr, node, ans)
        ans.pop()
        vis[node]=0

    dfs(1, 0, [])
    if g_len < float('inf'):
        print(g_len-1)
        print(*g_ans)
    else:
        print(-1)
        

                



    




# Set the stack size
threading.stack_size(1 << 27)

# Create and start the main thread
main_thread = threading.Thread(target=main)
main_thread.start()

# Wait for the main thread to complete
main_thread.join()

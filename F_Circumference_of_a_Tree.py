import sys, threading
input = sys.stdin.readline
from collections import defaultdict
inf = float('inf')
# returns the first number where key becomes true for a given delegate type key
def bs(low=1, high=1, key = lambda x: True):

    while low <= high:
        mid = (low + high)//2
        if key(mid):
            high = mid-1
        else:
            low = mid+1
    return low


def main():
    n = int(input())
    # 
    # nums =  list(map(int, input().split()))
    G = [[] for _ in range(n)]
    vis = [0]*n
    if n == 1:
        print(0)
        return
    for _ in range(n-1):
        u, v = list(map(int, input().split()))
        G[u-1].append(v-1)
        G[v-1].append(u-1)

    g_max = -inf
    def dfs(node):
        nonlocal g_max
        vis[node] = 1
        first_max = 0
        second_max = 0
        depth = 0
        for nbr in G[node]:
            if vis[nbr] == 0:
                cur_depth = dfs(nbr)
                if cur_depth > first_max:
                    second_max = first_max
                    first_max = cur_depth
                elif cur_depth > second_max:
                    second_max = cur_depth
                depth = max(depth, cur_depth)
        g_max = max(first_max + second_max + 1, depth, g_max)
        return depth
    
    dfs(0)
    print(2*g_max*3)
                



    




# Set the stack size
threading.stack_size(1 << 27)

# Create and start the main thread
main_thread = threading.Thread(target=main)
main_thread.start()

# Wait for the main thread to complete
main_thread.join()

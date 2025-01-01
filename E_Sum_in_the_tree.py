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
    par =  list(map(int, input().split()))
    s = list(map(int, input().split()))
    G = [[] for _ in range(n)]
    for i, u in enumerate(par):
        G[u-1].append(i+1)
        G[i+1].append(u-1)

    ans = 0
    vis = [0]*n
    def dfs(node, atleast, parity):
        nonlocal ans
        vis[node] = 1
        if 0 <= s[node] < atleast:
            return inf
        
        isLeaf = True
        for nbr in G[node]:
            if vis[nbr] == 0:
                isLeaf = False
                val = max(s[nbr], 0)
                if dfs(nbr, atleast+val, 1-parity) == inf:
                    return inf
        
    
    dfs(0, s[0])
    print(ans if ans < inf else -1)


    




# Set the stack size
threading.stack_size(1 << 27)

# Create and start the main thread
main_thread = threading.Thread(target=main)
main_thread.start()

# Wait for the main thread to complete
main_thread.join()

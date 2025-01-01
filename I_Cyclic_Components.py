import sys, threading
input = sys.stdin.readline
from collections import defaultdict, deque
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
    n, m =  list(map(int, input().split()))
    G = [[] for _ in range(n)]

    for _ in range(m):
        u, v =  list(map(int, input().split()))
        G[u-1].append(v-1)
        G[v-1].append(u-1)
    vis = [0]*n
    def bfs(node, seen):
        q = deque([node])
        seen.add(node)
        vis[node] =1
        # ind[node]+=1
        while q:
            x = q.popleft()
            for nbr in G[x]:
                if nbr not in seen:
                    vis[nbr] = 1
                    seen.add(nbr)
                    q.append(nbr)
    count = 0
    for i in range(n):
        seen = set()
        if vis[i] == 0:
            bfs(i, seen)
            for i in seen:
                # print(seen)
                if len(G[i]) != 2:
                    break
            else:
                count+=1

    print(count)


    




# Set the stack size
threading.stack_size(1 << 27)

# Create and start the main thread
main_thread = threading.Thread(target=main)
main_thread.start()

# Wait for the main thread to complete
main_thread.join()

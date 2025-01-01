from heapq import heappop, heappush
import sys, threading
input = sys.stdin.readline
from collections import defaultdict
input = sys.stdin.readline

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
    V, E =  list(map(int, input().split()))
    G = [[] for _ in range(V+1)]
    for _ in range(E):
        u, v, w = list(map(int, input().split()))
        G[u].append([v, w])
        G[v].append([u, w])

    pq = [(0, 1, [])]
    seen = set()
    path = []
    # print(G)
    while pq:
        w, node, path = heappop(pq)
        path.append(node)
        if node == V:
            print(*path)
            return
        if node in seen:
            continue
    
        seen.add(node)
        for nbr, wei in G[node]:
            f = 1
            heappush(pq, (w+wei, nbr, path[:]))

    print(-1)               
        
    

main()
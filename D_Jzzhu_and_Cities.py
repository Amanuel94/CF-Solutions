import sys, threading
input = sys.stdin.readline
from collections import defaultdict
input = sys.stdin.readline
from heapq import heapify, heappop, heappush
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
    n,m,k =  list(map(int, input().split()))
    graph = defaultdict(list)
    for _ in range(m):
        u, v, x = list(map(int, input().split()))
        graph[u].append([v, x])
        graph[v].append([u, x])
    

    heap = [(0, 1)]
    vis = set([1])
    dp = [inf]*n
    dp[0] = 0
    
    while heap:
        w, node = heappop(heap)
        vis.add(node)
        for nbr,x in graph[node]:
            if nbr not in vis:
                dp[nbr-1] =  min(w + x, dp[nbr-1])
                heappush(heap, (w + x, nbr))
    ans = 0
    for _ in range(k):
        s, y  = list(map(int, input().split()))
        if y >= dp[s-1]:
            ans+=1
    print(ans)




    


main()
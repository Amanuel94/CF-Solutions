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


def dfs(node, graph, vis, k, x):
    vis.add(node)
    des = 0
    deleted = 0
    for nbr in graph[node]:
        if nbr not in vis:
            below, prev = dfs(nbr, graph, vis, k, x)
            deleted += prev
            if below >= x: 
                deleted += 1
                des -= below
            des += below
        
    des += 1
    return des, deleted

def good(graph, vis, k, x):
    b, ans = dfs(0, graph, vis, k, x)
    if ans == k and b >= x:
        return False
    if ans > k :
        return False
    return True
    
def main():
    t = int(input())
    for _ in range(t):
        n,k =  list(map(int, input().split()))
        g = [[] for i in range(n)]
        for __ in range(n-1):
            u, v = list(map(int, input().split()))
            g[u-1].append(v-1)
            g[v-1].append(u-1)
        
        res = bs(1, 2**31-1, lambda x: good(g, set(), k, x))
        print(res-1)
        # if k == 298:
        #     print("here")
        
    
        
        

            


    

    

main()

sys.setrecursionlimit(10**6)

# # Set the stack size
# threading.stack_size(1 << 27)

# # Create and start the main thread
# main_thread = threading.Thread(target=main)
# main_thread.start()

# # Wait for the main thread to complete
# main_thread.join()

import sys, threading
input = sys.stdin.readline
from collections import defaultdict, deque
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

    n, m = list(map(int, input().split()))
    cats =  list(map(int, input().split()))

    graph = [[] for _ in range(n+1)]
    for _ in range(n-1):
        u, v = list(map(int, input().split()))
        graph[u].append(v)
        graph[v].append(u)

    seen = [0]*n
    def dfs(node, seen, m,  n_cats):
        count = 0
        seen[node-1] = 1
        isleaf = 1
        if cats[node-1]:    
            n_cats+=1
        else:
            n_cats = 0
            
        if n_cats > m:
            return 0 
        
        for nbr in graph[node]:
            if seen[nbr-1] == 0:
                isleaf = 0
                count+=dfs(nbr,seen, m, n_cats)
        count+=isleaf

        return count


    def bfs(start, seen,  m, n_cats):
        queue = deque([(start, 0, 0)])  # (node, n_cats, depth)
        seen = [0] * n
        seen[0] = 1
        count = 0

        while queue:
            node, n_cats, depth = queue.popleft()
            isleaf = 1

            if cats[node-1]:
                n_cats += 1
            else:
                n_cats = 0

            if n_cats > m:
                continue

            for nbr in graph[node]:
                if not seen[nbr-1]:
                    seen[nbr-1] = 1
                    isleaf = 0
                    queue.append((nbr, n_cats, depth + 1))

            count += isleaf

        return count



                    
    print(bfs(1, seen, m, 0))

    




# Set the stack size
threading.stack_size(10**6)

# Create and start the main thread
main_thread = threading.Thread(target=main)
main_thread.start()

# Wait for the main thread to complete
main_thread.join()







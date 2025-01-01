import sys, threading
input = sys.stdin.readline
from collections import defaultdict
input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        p =  list(map(int, input().split()))
        G = defaultdict(list)
        A = [0]*n 
        root = 0
        for i in range(n):
            if p[i]!= i:
                G[i+1].append(p[i])
                G[p[i]].append(i+1)
            else:
                root = i
        def dfs(node, vis):
            vis.add(node)
            ans = 0
            for nbr in G[node]:
                A[node-1] = max(A[node-1], dfs(nbr, vis))
            A[node-1]+=1
            return A[node-1]
        
        for i in range(1, n):
            G[i].sort(key = lambda x: A[x-1], reverse= True)

        dfs(root, set())
        paths = []
        def DFS(node, vis, path):
            vis.add(node)
            if len(G[node]) == 1:
                paths.append(path)
            for nbr in G[node]:
                path.append(nbr)
                path.extend(dfs(nbr, vis, path))
                path = []
            return path
        DFS(root, set(), [])
        print(paths)
            


            
            


    




# Set the stack size
threading.stack_size(1 << 27)

# Create and start the main thread
main_thread = threading.Thread(target=main)
main_thread.start()

# Wait for the main thread to complete
main_thread.join()

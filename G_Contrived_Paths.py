import sys, threading
input = sys.stdin.readline
from collections import defaultdict, deque
input = sys.stdin.readline

def main():
    n,m , k =  list(map(int, input().split()))
    a =  list(map(int, input().split()))
    G = defaultdict(list)
    
    for _ in range(m):
        x, y, w = list(map(int, input().split()))
        G[x].append([y, w])
        G[y].append([x, w])
    b = list(map(int, input().split()))

    for i in range(1, n+1):
        # G[i].append([n+1, a[i-1]])
        G[n+1].append([i, a[i-1]])
    n+=1
    # smallest = sorted(list(range(n)), key = lambda x:a[x])[0]
    a.append(0)
    # print(n)
    for i, bi in enumerate(b):
        dist = [float('inf') for i in range(n)]
        q = deque([[bi, 0]])
        # carry = 0
        while q:
            x, w = q.popleft()
            dist[x-1] = min(dist[x-1], w)
            for nbr, wn in G[x]:
                s = w + wn 
                if dist[nbr-1] > s:
                    q.append([nbr, s])
            if dist[-1] > w + a[x-1]:
                q.append([n, w + a[x-1]])
                
        print(*dist[:-1])
        





    
    




# Set the stack size
threading.stack_size(1 << 27)

# Create and start the main thread
main_thread = threading.Thread(target=main)
main_thread.start()

# Wait for the main thread to complete
main_thread.join()

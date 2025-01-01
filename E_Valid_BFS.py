import sys, threading
input = sys.stdin.readline
from collections import defaultdict, deque

def main():
    n = int(input())
    G = defaultdict(set)
    for _ in range(n-1):
        x, y =  list(map(int, input().split()))
        G[x].add(y)
        G[y].add(x)
    bfs = list(map(int, input().split()))
    vis = set()
    f = 1
    G[1].add(1)
    if bfs[0] != 1:
        print("No")
    else:
        i = 1
        q = deque([1])
        vis = set([1])
        # print(dict(G))
        while q:
            x = q.popleft()
            vis.add(x)
            for j in range(len(G[x])-1):
                if bfs[i] not in G[x]:
                    print("No")
                    f = 0
                    break
                else:
                    q.append(bfs[i])
                    i+=1
            if not f:
                break
            
        if f:
            print("Yes")

    




# Set the stack size
threading.stack_size(1 << 27)

# Create and start the main thread
main_thread = threading.Thread(target=main)
main_thread.start()

# Wait for the main thread to complete
main_thread.join()

import sys, threading
input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        g =  list(map(int, input().split()))
        s = input().strip()
        G = defaultdict(list)
        inc = [0]*n
        for v, p in enumerate(g):
            G[v+2].append(p)
            inc[p-1]+=1

        color = [[0,0] for i in range(n)]
        q = deque([i+1  for i in range(n) if inc[i] == 0])
        

        count = 0
        while q:
            x = q.popleft()
            
            if s[x-1]=='W':
                color[x-1][1]+=1
            else:
                color[x-1][0]+=1
            if color[x-1][0] == color[x-1][1]:
                count+=1
            
            for nbr in G[x]:
                inc[nbr-1]-=1
                if inc[nbr-1] == 0:
                    q.append(nbr)
                color[nbr-1][0]+=color[x-1][0]
                color[nbr-1][1]+=color[x-1][1]
        print(count)



    




# Set the stack size
threading.stack_size(1 << 27)

# Create and start the main thread
main_thread = threading.Thread(target=main)
main_thread.start()

# Wait for the main thread to complete
main_thread.join()

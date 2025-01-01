import sys, threading
input = sys.stdin.readline
from collections import defaultdict
input = sys.stdin.readline

def main():
    
    n, m, k =  list(map(int, input().split()))
    x = set(map(int, input().split()))
    edges = []
    for _ in range(m):
        edges.append(list(map(int, input().split())))
    
    edges.sort(key=lambda x:x[2])
    specials = {i:(lambda k: int(k in x))(i) for i in range(1, n+1)}
    p = {i:i for i in range(1,n+1)}
    def getP(i):
        if i == p[i]:
            return i
        p[i] = getP(p[i])
        return p[i]
        # print(specials)
        # print(specials)
        # print(p)
    c = 0
    for u,v,w in edges:

        if getP(u) != getP(v):
                # print(getP(u), getP(v), specials[getP(u)],  specials[getP(v)])
            
            specials[getP(v)]+=specials[getP(u)]
            p[getP(u)] = getP(v)
            
            if specials[getP(v)] >= k:
                print(*([w]*k))
                break

# Set the stack size
threading.stack_size(10**6)

# Create and start the main thread
main_thread = threading.Thread(target=main)
main_thread.start()

# Wait for the main thread to complete
main_thread.join()

import sys, threading
sys.setrecursionlimit(10**7)

def main():
    n, m =  list(map(int, input().split()))
    p = {i:i for i in range(1, n+1)}
    def getP(i):
        if i == p[i]:
            return i
        p[i] = getP(p[i])
        return p[i]

        # parent = p[x]
        # while p[parent] != parent:
        #     parent = p[parent]
            
        # while x != p[x]:
        #     p[x] = parent
        #     x = p[x]
                
        # return parent


    size = {i:1 for i in range(1, n+1)}
    edges = {i:0 for i in range(1, n+1)}
    for _ in range(m):
        u,v = list(map(int, input().split()))
        if getP(u) != getP(v):
            size[getP(v)]+=size[getP(u)]
            edges[getP(v)]+=(edges[getP(u)])
            p[getP(u)] = getP(v)
        edges[getP(v)]+=1
    def f():
        for i in range(1, n+1):
            x, y = edges[getP(i)], size[getP(i)]
            if x != y*(y-1)//2:
                return False
        return True
    if f():
        print('YES')
    else:
        print('NO')

# Set the stack size
threading.stack_size(1 << 27)

# Create and start the main thread
main_thread = threading.Thread(target=main)
main_thread.start()

# Wait for the main thread to complete
main_thread.join()


    


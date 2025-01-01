import sys, threading
input = sys.stdin.readline
input = sys.stdin.readline


def inBound(i, j, n, m):
    return 0<=i<n and 0<=j<m

def main():

    

    n, m =  list(map(int, input().split()))
    grid = []
    for _ in range(n):
        grid.append([*input().strip()])
    directions = [(1,0), (0,1), (0,-1), (-1, 0)]
    p = {(i,j):[(i,j),1] for i in range(n) for j in range(m)}
    # c = {(i,j): 1 for  i in range(n) for j in range(m)}

    def getP(t):
        if p[t][0] == t:
            return p[t]
        p[t] = getP(p[t][0])
        return p[t]

    for i in range(n):
        for j in range(m):
            if grid[i][j] == '.':
                for dx, dy in directions:
                    if inBound(i+dx, j+dy, n, m) and grid[i+dx][j+dy] == '.' and getP((i+dx, j+dy)) != getP((i,j)):
                        getP((i,j))[1]+=getP((i+dx, j+dy))[1]
                        p[getP((i+dx, j+dy))[0]][0] = getP((i,j))[0]
    

    for i in range(n):
        for j in range(m):
            if grid[i][j] == '*':
                grid[i][j] = 1
                ads = set()
                for dx, dy in directions:
                    if inBound(i+dx, j+dy, n, m) and grid[i+dx][j+dy] == '.':
                        ads.add(tuple(getP((i+dx, j+dy))))
                for x, y in ads:
                    grid[i][j]+=y
                    grid[i][j]%=10
            
    for c in grid:
        print("".join(map(str, c)))
                    
                        


                        
        

# Set the stack size
threading.stack_size(10**6)

# Create and start the main thread
main_thread = threading.Thread(target=main)
main_thread.start()

# Wait for the main thread to complete
main_thread.join()

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


def main():
    t = int(input())
    for _ in range(t):
        n, m =  list(map(int, input().split()))
        grid = []
        for k in range(n):
            grid.append(list(input()))
    
    def inBound(i, j):
        nonlocal n, m
        return 0 <= i < n and 0 <= j < m
    
    vis = [[0]*m for _ in range(n)]
    def blockDfs(row,col):
        if vis[row][col] or grid[row][col] == "#":
            return
        vis[row][col] = 1
        for dx,dy in [[1,0],[0,1],[-1,0],[0,-1]]:
            crow = dx + row
            ccol = dy + col
            if inBound(crow, ccol) and grid[crow][ccol] == '.':
                grid[crow][ccol] = '#'
            elif inBound(crow, ccol) and grid[crow][ccol] == "B":
                blockDfs(crow, ccol)
    
    def moveDFS(row, col):
        nonlocal n, m
        if row ==  n-1 and col == m - 1:
            return True
        
        
        vis[row][col] = 1
        for dx,dy in [[1,0],[0,1],[-1,0],[0,-1]]:
            crow = dx + row
            ccol = dy + col
            if inBound(crow, ccol) and  vis[crow][ccol] == 0 and grid[crow][ccol] == '.':
                if moveDFS(crow, ccol):
                    return True

            elif inBound(crow, ccol) and grid[crow][ccol] == "B":
                return False






# Set the stack size
threading.stack_size(1 << 27)

# Create and start the main thread
main_thread = threading.Thread(target=main)
main_thread.start()

# Wait for the main thread to complete
main_thread.join()

import sys
input = sys.stdin.readline
from collections import deque


n,m = list(map(int, input().split()))
directions = [(1,0), (-1,0), (0,1), (0,-1)]
grid = []
for _ in range(n-1):
    grid.append(list(input()[:-1]))  
grid.append(list(input()))

vis = set()
def in_bound(i, j):
    return 0 <= i < n and 0 <= j < m



def bfs(node, c):
    xo, yo = node
    # grid[xo][yo] = c
    q = deque([node])
    while q:
        x, y = q.popleft()
        if len(grid[x][y])==2:
            return True
        grid[x][y] = c + '.'
        for dx, dy in directions:
            tx, ty = x+dx, y+dy
            if in_bound(tx, ty) and grid[tx][ty] == c:
                # grid[tx][ty] = c+'.'
                q.append((tx, ty))
    return False
ans = False

def func():
    for i, r in enumerate(grid):
        for j, c in enumerate(r):
            if len(c) == 1:
                if bfs((i, j), c):
                   return 'Yes'
            
    return 'No'

# bfs((0,0), grid[0][0])
# print(grid)

print(func())
                    


            




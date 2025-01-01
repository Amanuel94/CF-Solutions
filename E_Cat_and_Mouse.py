import sys
input = sys.stdin.readline
n, m , p = list(map(int, input().split()))
from collections import deque
q = deque()
directions = [(1,0), (0,1), (0, -1), (-1, 0), (0, 0)]
moves = {
    0: (0,0),
    1:(1,0),
    2: (-1,0),
    3:(0,-1),
    4:(0, 1)
}
grid = []
start = (0,0)
for i in range(n):
    x = input()
    grid.append(x)
    for j, ind in enumerate(x):
        if ind == '.':
            q.append((i, j))
        elif ind == 'M':
            start=  (i,j)
seq = list(map(int, input().split()))
ans = 0
def isValid(i, j):
    return 0<=i< n and 0<=j<m and grid[i][j] != '#' 
while q:
    lvl = len(q)
    for _ in range(lvl):
        x , y = q.popleft()
        if grid[x][y] == 'M':
            ans+=1
        for move in moves:
            dx, dy = moves[move]
            if isValid(x+dx, y+dy):
                q.append((x+dx, y+dy))
        grid[i][j] = 
        
print(ans)



        
        



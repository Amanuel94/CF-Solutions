import sys
input = sys.stdin.readline
from collections import deque

t = int(input())

directions = [(1,0), (-1, 0), (0, 1), (0, -1), (1, -1), (-1, 1), (-1, -1), (1,1)]
for _ in range(t):
    n = int(input())
    grid = [input(), input()]
    # print(grid)
    def bfs():
        que = deque([(0,0)])
        vis = set([(0,0)])

        while que:
            lvl = len(que)
            # print(que)
            for _ in range(lvl):
                x, y = que.popleft()
                if x == 1 and y ==  n-1:
                    return True
                for dx, dy in directions:
                    if 0 <= x+dx < 2 and 0 <= y+dy< n and grid[x+dx][y+dy] == '0' and  (x+dx, y+dy) not in vis:
                        que.append((x+dx, y+dy))
                        vis.add((x+dx, y+dy))
        return False
    bo = bfs()
    if bo:
        print('YES')
    else:
        print('NO')
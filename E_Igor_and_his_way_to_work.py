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
    n, m =  list(map(int, input().split()))
    grid = []
    S = T = (-1, -1)
    for i in range(n):
        grid.append(list(input().strip()))
        try:
            s = grid[-1].index("S")
            S = (i , s)
        except:
            pass
        
        try:
            t = grid[-1].index("T")
            T = (i , t)
        except:
            pass
    # print(grid)
    def inBound(i, j):
        nonlocal n, m
        return 0 <= i < n and 0 <= j < m
    
    dirs = [(1, 0), (0, 1), (0, -1), (-1, 0)]

    for dx, dy in dirs:
        x, y = S
        # print(x+dx, y+dy)
        while inBound(x+dx, y+dy) and grid[x+dx][y+dy] != "*":
            if grid[x+dx][y+dy] == "T":
                print("YES")
                return
                
            grid[x+dx][y+dy] = "S"
            x, y = x+dx, y+dy

    ortho  = {
        (1, 0) : [(0, 1), (0, -1)],
        (-1, 0): [(0, 1), (0, -1)],
        (0, 1) : [(1, 0), (-1, 0)],
        (0, -1): [(1, 0), (-1, 0)]
    }
    # print(grid)
    for dx, dy in dirs:
        x, y = T
        # x+=dx
        # y+=dy
        while inBound(x, y) and grid[x][y] != "*":
            if grid[x][y] == "S":
                print("YES")
                return 
            # grid[x+dx][y+dy] = "T"               
            # x, y = x+dx, y+dy
            sx, sy = x, y
            for tx, ty in ortho[(dx, dy)]:   
                sx, sy = x, y
                # sx+=tx
                # sy+=ty
                while inBound(sx, sy) and grid[sx][sy] != "*":
                    if grid[sx][sy] == "S":
                        print("YES")
                        return 
                    sx+=tx
                    sy+=ty

            x+=dx
            y+=dy
            
        for tx, ty in ortho[(dx, dy)]:  
            while inBound(sx, sy) and grid[sx][sy] != "*":
                if grid[sx][sy] == "S":
                    print("YES")
                    return 
                sx+=tx
                sy+=ty
        
    
    # print(g   rid)
    print("NO")
            
    

main()

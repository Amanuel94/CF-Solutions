
def main():
    n, m =  list(map(int, input().split()))
    grid = [[0]*102 for _ in range(102)]
    for _ in range(n):
        x, y = list(map(int, input().split()))
        grid[x+1][y+1]+=1
    
    for i in range(101):
        for j in range(101):
            grid[i+1][j+1] += grid[i+1][j]+grid[i][j+1] - grid[i][j]
    
    for _ in range(m):
        sx, sy, ex,ey = list(map(int, input().split()))
        print(grid[ex+1][ey+1] - grid[ex+1][sy] - grid[sx][ey+1] + grid[sx][sy])

main()
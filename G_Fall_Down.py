t  = int(input())

for _ in range(t):
    n, m = list(map(int,input().split()))
    grid = []
    for __ in range(n):
        grid.append(list(input()))

    def nextValid(row, col, grid):
        i = row
        while i < len(grid):
            if grid[i][col] == '.':
                return i
            elif grid[i][col] == 'o':
                return row
            i+=1
        return row


    i = 0
    while i < n-1:
        j = 0
        while j < m:
            if grid[i][j] == '*':
                row = nextValid(i, j, grid)
                if grid[row][j] == '.':
                    grid[i][j], grid[row][j] = grid[row][j], grid[i][j]
            j+=1
        i+=1

    for row in grid:
        print("".join(row))
    # print()        


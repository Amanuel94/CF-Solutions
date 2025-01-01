import sys, threading
input = sys.stdin.readline
from collections import defaultdict
inf = float('inf')
MOD = 10**9 + 7
# returns the first number where key becomes true for a given delegate type key
def bs(low=1, high=1, key = lambda x: True):

    while low <= high:
        mid = (low + high)//2
        if key(mid):
            high = mid-1
        else:
            low = mid+1
    return low

def inBound(i, j):
    return 0 <= i <  3  and 0 <= j < 3 


def main():

    grid = []
    grid.append(list(input().strip()))
    grid.append(list(input().strip()))
    grid.append(list(input().strip()))
    dirs = [(0,1), (1,0), (0,-1),(-1,0), (-1,1), (-1,-1), (1,-1), (1,1)]

    def backtrack(i, j, l):
        if l == 0:
            return ""
        
        min_ = "Y"
        cur = grid[i][j]
        grid[i][j] = "Z"
        for dx, dy in dirs:
            tx, ty = i+dx, j+dy
            if inBound(tx, ty) and grid[tx][ty] < min_:
                min_ = grid[tx][ty]
        ans = "ZZZZZZZZ"
        for dx, dy in dirs:
            tx, ty = i+dx, j+dy
            if inBound(tx, ty) and grid[tx][ty] == min_:
                ans = min(ans, cur + backtrack(tx, ty, l-1))
        grid[i][j] = cur
        return ans
    ans = "Z"
    for i in range(3):
        for j in range(3):
            ans = min(ans, backtrack(i, j, 3))
    print(ans)
            

        


    
    




# Set the stack size
threading.stack_size(1 << 27)

# Create and start the main thread
main_thread = threading.Thread(target=main)
main_thread.start()

# Wait for the main thread to complete
main_thread.join()

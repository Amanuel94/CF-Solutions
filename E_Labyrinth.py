import sys, threading
input = sys.stdin.readline
from collections import defaultdict, deque
input = sys.stdin.readline

# returns the first number where key becomes true for a given delegate type key
def bs(low=1, high=1, key = lambda x: True):

    while low <= high:
        mid = (low + high)//2
        if key(mid):
            high = mid-1
        else:
            low = mid+1
    return low


def inBound(i, j, n, m):
    return 0<=i<n and 0<=j<m


def main():
    n,m =  list(map(int, input().split()))
    r,c = list(map(int, input().split()))
    x,y = list(map(int, input().split()))

    D, R, L, U = (1,0), (0,1), (0,-1), (-1, 0)

    directions = [U, D, L, R]
    grid = []
    for _ in range(n):
        grid.append(list(input().strip()))
    
    queue = deque([((r-1, c-1), x, y)])
    # seen = set([(r-1, c-1)])
    seen = [[0]*m for _ in range(n)]
    seen[r-1][c-1] = 1
    ans = 0
    res = []
    while queue:
        node, xi, yi = queue.popleft()
        print((node, xi, yi))
        ans+=1


        for dir_ in directions:
            tx, ty = node[0] + dir_[0], node[1] + dir_[1]
            if dir_ == L and xi and inBound(tx, ty, n, m) and grid[tx][ty] == '.' and not seen[tx][ty]:
                seen[tx][ty] = 1
                queue.append(((tx, ty), xi-1, yi))
            
            if dir_ == R and yi and inBound(tx, ty, n, m) and grid[tx][ty] == '.' and not seen[tx][ty]:
                seen[tx][ty] = 1
                queue.append(((tx, ty), xi, yi-1))
            
            elif dir_ == U or dir_ == D:
                if inBound(tx, ty, n, m) and grid[tx][ty] == '.' and not seen[tx][ty]:
                    seen[tx][ty] = 1
                    queue.append(((tx, ty), xi, yi))
            elif xi == 0
            # seen[tx][ty] = 1
    print(ans)

    print(sorted(res))
                

    




# Set the stack size
threading.stack_size(1 << 27)

# Create and start the main thread
main_thread = threading.Thread(target=main)
main_thread.start()

# Wait for the main thread to complete
main_thread.join()

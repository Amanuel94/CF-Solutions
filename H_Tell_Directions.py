import sys, threading
input = sys.stdin.readline
from collections import defaultdict
inf = float('inf')
MOD = 10**9 + 7

def si():
    return input().strip()
def ii():
    return int(input())
def lsi():
    return input().strip().split()
def mi():
    return map(int, input().split())
def li():
    return list(map(int, input().split()))

def SieveOfEratosthenes(n):
    prime = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    prime[0]= False
    prime[1]= False
    return prime

def YN(b):
    return "YES" if b else "NO"

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
    return 0 <= i < n and 0 <= j < m

def dfs(node,grid, path, k):
    if len(path) > k:
        return False

    x, y = node
    if inBound(x, y, len(grid), len(grid[0])) and grid[x][y] == "X" and len(path) == k:
        return True
    dir = {
        "D":(1, 0),
        "L":(0, -1),
        "R":(0, 1),
        "U":(-1, 0)
    }
    for d in "DLRU":
        dx, dy = dir[d]
        tx, ty = x+dx, y + dy
        if inBound(tx, ty, len(grid), len(grid[0])):
            if grid[tx][ty] in "X.":
                path.append(d)
                if dfs((tx, ty),grid, path, k) :
                    return True
                path.pop()
    return False


def main():
    n, m, k  = li()
    grid = []
    sr = sc = -1
    for r in range(n):
        row = list(si())
        if "X" in row:
            sr = r
            sc = row.index("X")
        grid.append(row[::])
    path = []

    if dfs((sr, sc), grid, path, k):
        print(*path, sep = "")
    else:
        print("IMPOSSIBLE")







# Set the stack size
threading.stack_size(1 << 27)

# Create and start the main thread
main_thread = threading.Thread(target=main)
main_thread.start()

# Wait for the main thread to complete
main_thread.join()
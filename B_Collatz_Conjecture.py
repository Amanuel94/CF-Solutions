from functools import cache
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

# 1 2 .. y - 1
# 1 2 3 4 5
#   1 2 3
# 4 5 6 7
# 8 9 0 1
# 2 2 1

# 16 3 2  17 2

# 1 2
#   1
# 2 3

def solve(x, y, k):
    

    if k == 0:
        return x
    if x < y:
        return  (x-1 + k)%(y-1) + 1
    
    req =  ((-x)%y)
    if req > k:
        return (x + k)//y if (x+k)%y == 0 else  x + k
    x += req
    while x%y == 0:
        x//=y
    return solve(x, y, k - req)
    


def main():
    t = int(input())
    for _ in range(t):
        x, y, k =  list(map(int, input().split()))
        if x%y == 0 and k > 0:
            x+=1
            k-=1
        print(solve(x, y, k))
    




# Set the stack size
threading.stack_size(1 << 27)

# Create and start the main thread
main_thread = threading.Thread(target=main)
main_thread.start()

# Wait for the main thread to complete
main_thread.join()

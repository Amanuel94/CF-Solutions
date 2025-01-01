import copy
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


def main():
    t = int(input())
    
    for _ in range(t):
        f = True
        n, m =  list(map(int, input().split()))
        tile = []
        for __ in range(n):
        
            tile = []
            tile.append(list(map(int, input().split())))
            tile.append(list(map(int, input().split())))
            # print(tile)
            if tile[0][1] == tile[1][0]:
                f = False
        a = "NO" if f or m%2 else "YES"
        print(a)
            
       
    




# Set the stack size
threading.stack_size(1 << 27)

# Create and start the main thread
main_thread = threading.Thread(target=main)
main_thread.start()

# Wait for the main thread to complete
main_thread.join()

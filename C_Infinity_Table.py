import math
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
    t = int(input())
    for _ in range(t):
        k =  int(input())
        r, r1 = int(math.sqrt(k)), int(math.sqrt(k))+1
        ind = k - r**2
        if ind == 0:
            print(r, 1)
            continue
        if ind > (r1**2 - r**2)//2 +1:
            row = r1
            col = r1 - (ind - r1)
        else:
            row = ind
            col = r1
        print(row, col)
        






# Set the stack size
threading.stack_size(1 << 27)

# Create and start the main thread
main_thread = threading.Thread(target=main)
main_thread.start()

# Wait for the main thread to complete
main_thread.join()

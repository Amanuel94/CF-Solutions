import sys, threading
input = sys.stdin.readline
from collections import defaultdict
import math
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
def good(mid, n, x, y):
    return (mid//x + mid//y) >=  n
def main():
    n, x, y =  list(map(int, input().split()))
    # if n == 1:
        # print(min(x,y))
    print(bs(0, n*min(x), lambda k: good(k, n-1,x, y)) + min(x, y))
    # print(bs(0, n, lambda k: good(k, n-1,x, y)))


    

            

    




# Set the stack size
threading.stack_size(1 << 27)

# Create and start the main thread
main_thread = threading.Thread(target=main)
main_thread.start()

# Wait for the main thread to complete
main_thread.join()

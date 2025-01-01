import sys, threading
input = sys.stdin.readline
from collections import defaultdict
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

# 4 5 2 1 3 5
# 4 5 2 1 2 5
# 4 5 3 2 1 2 5
# 4 5 

# dp(L, R, 0)  is the least moves required to make the segment having color cL.
# dp(L, R, 1)  is the least moves required to make the segment having color cR.
# dp(L, R, 0) = dp(L-1)
# abcdef
# abcd**


def main():
    t = int(input())
    nums =  list(map(int, input().split()))
    




# Set the stack size
threading.stack_size(1 << 27)

# Create and start the main thread
main_thread = threading.Thread(target=main)
main_thread.start()

# Wait for the main thread to complete
main_thread.join()

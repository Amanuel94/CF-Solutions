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
        n = int(input())
        a =  list(map(int, input().split()))
        min_ind, max_ind = -1, -1
        min_, max_ = inf, -inf
        for i, ai in enumerate(a):
            if ai < min_:
                min_ = ai
                min_ind = i+1
            
            if ai > max_:
                max_ = ai
                max_ind = i+1
        # print(min(max_ind, min_ind, min_ind + n - max_ind +1, max_ind + n - min_ind +1))
        print(min(max(max_ind, min_ind), n - max_ind+1 + min_ind, n - min_ind+1 + max_ind, max(n - min_ind+1, n - max_ind+1)))
    




# Set the stack size
threading.stack_size(1 << 27)

# Create and start the main thread
main_thread = threading.Thread(target=main)
main_thread.start()

# Wait for the main thread to complete
main_thread.join()

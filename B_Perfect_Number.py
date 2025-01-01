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

    def helper(l, s):

        if l == 1:
            return int(s < 10)
        if s < 0:
            return 0

        ans = 0
        first = int(str(s)[0])
        n = len(str(s))
        for i in range(1, first):
            ans+=helper(n-1, s - first)


# Set the stack size
threading.stack_size(1 << 27)

# Create and start the main thread
main_thread = threading.Thread(target=main)
main_thread.start()

# Wait for the main thread to complete
main_thread.join()

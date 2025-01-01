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

# 5 4 3 1 2
# 2 5
# 25 - 
# 10 9 8 1 2 3 4 5 6
def main():
    t = int(input())
    for _ in range(t):
        n, m, k =  list(map(int, input().split()))
        print(*([n - i for i in range(n-m )] + [i for i in range(1, m+1)]))
    




# Set the stack size
threading.stack_size(1 << 27)

# Create and start the main thread
main_thread = threading.Thread(target=main)
main_thread.start()

# Wait for the main thread to complete
main_thread.join()

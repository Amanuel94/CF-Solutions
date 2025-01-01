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
        n, k =  list(map(int, input().split()))
        cols = [i for i in range(1, n+1)]
        cur = 1
        q = 1
        cliques = []
        for c in cols:
            if c > cur + k//2:
                cur = c
                q+=1
            cliques.append(q)
        
        print(*cols)
        print(q)
        print(*cliques)
    




# Set the stack size
threading.stack_size(1 << 27)

# Create and start the main thread
main_thread = threading.Thread(target=main)
main_thread.start()

# Wait for the main thread to complete
main_thread.join()

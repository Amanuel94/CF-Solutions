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
        c =  list(map(int, input().split()))

        first = c.count(c[0])
        if first < k:
            print("NO")
            continue
        if c[-1] == c[0]:
            print("YES")
            continue
        i = 0
        fc = 0
        while fc < k:
            if c[i] == c[0]:
                fc += 1
            i+=1
        last = c[i:].count(c[-1])
  
        if first >= k and last >= k:
            print("YES")
        else:
            print("NO")
            
    




# Set the stack size
threading.stack_size(1 << 27)

# Create and start the main thread
main_thread = threading.Thread(target=main)
main_thread.start()

# Wait for the main thread to complete
main_thread.join()

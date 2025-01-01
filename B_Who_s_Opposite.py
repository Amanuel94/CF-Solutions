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
        a, b, c =  list(map(int, input().split()))
        a, b  = max(a, b), min(a, b)
        diff = a - b
        if b > diff or a < diff or c > 2*diff:
            print(-1)
            continue
        # c1 =  c + diff
        # c2 = c - diff
        # n = 2*diff
        # if c > 2*diff or c < 1:
        #     print(-1)
        #     continue
        # if c <= diff and 2*diff >= c1 >= diff:
        #     if c1 not in [a, b]: print(c1)
        #     else: print(-1)
        # elif c > diff and 1 <= c2 < diff:
        #     if c2 not in [a, b]: print(c2)
        #     else: print(-1)
        # else:
        #     print(-1)
        if c <= diff:
            print(c + diff)
        else:
            print(c - diff)




    




# Set the stack size
threading.stack_size(1 << 27)

# Create and start the main thread
main_thread = threading.Thread(target=main)
main_thread.start()

# Wait for the main thread to complete
main_thread.join()

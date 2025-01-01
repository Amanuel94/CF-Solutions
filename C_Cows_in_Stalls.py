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


def helper(mid, stalls, cows):

    prev = -inf
    for i in range(len(stalls)):
        if cows == 0:
            break
        if stalls[i] - prev >= mid:
            cows -= 1
            prev = stalls[i]
        
        if cows == 0: return False
    
    return True


        




def main():
    n, cows =  list(map(int, input().split()))
    stalls =  list(map(int, input().split()))

    print(bs(1, max(stalls), lambda x: helper(x, stalls, cows))-1)
    




# Set the stack size
threading.stack_size(1 << 27)

# Create and start the main thread
main_thread = threading.Thread(target=main)
main_thread.start()

# Wait for the main thread to complete
main_thread.join()

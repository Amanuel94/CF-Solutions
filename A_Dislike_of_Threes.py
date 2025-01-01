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


precomp = [0]*1002
i = 0
cur = 1
while i < len(precomp):
    while cur%3 == 0 or cur%10 == 3:
        cur +=1
    precomp[i] = cur
    cur+=1
    i+=1



def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(precomp[n-1])
    




# Set the stack size
threading.stack_size(1 << 27)

# Create and start the main thread
main_thread = threading.Thread(target=main)
main_thread.start()

# Wait for the main thread to complete
main_thread.join()

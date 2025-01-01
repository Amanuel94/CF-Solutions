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


def main():
    n = int(input())
    h = [0] + list(map(int, input().split()))
    pre = 0
    diff = [h[k]- h[k+1] for k in range(n)]
    count = 0
    for i in range(n):
        pre = pre + diff[i] 
        # print(pre)
        if pre < 0:
            count-=pre
            pre = 0
    print(count)
    




# Set the stack size
threading.stack_size(1 << 27)

# Create and start the main thread
main_thread = threading.Thread(target=main)
main_thread.start()

# Wait for the main thread to complete
main_thread.join()

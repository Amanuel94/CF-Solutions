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
    n = int(input())
    nums =  list(map(int, input().split()))
    nums.sort()
    pre = [0]
    for i in range(n):
        pre.append(pre[-1]+nums[i])
    for i in range(1, n+1):
        # print(nums[i-1], pre[i-1]+1)
        if nums[i-1] > pre[i-1]+1:
            print(pre[i-1]+1)
            break
    else:
        print(pre[-1]+1)


    




# Set the stack size
threading.stack_size(1 << 27)

# Create and start the main thread
main_thread = threading.Thread(target=main)
main_thread.start()

# Wait for the main thread to complete
main_thread.join()

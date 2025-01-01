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
    t = int(input())
    for _ in range(t):
        n = int(input())
        nums =  list(map(int, input().split()))
        nums.sort()

        i = 1
        count = 1
        while i < n:
            # print(nums[i], nums[i-1])
            if nums[i]-nums[i-1] > 1:
                count+=1
            i+=1
        print("YES") if count < 2 else print("NO")

    




# Set the stack size
threading.stack_size(1 << 27)

# Create and start the main thread
main_thread = threading.Thread(target=main)
main_thread.start()

# Wait for the main thread to complete
main_thread.join()

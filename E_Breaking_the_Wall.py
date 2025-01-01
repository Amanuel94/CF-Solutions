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


def check(mid, nums):
    
    s1, s2 = inf, inf
    prev = inf
    for num in nums: 

        if num < s1:
            s2 = s1
            s1 = num
        elif num < s2:
            s2 = num
        if num + prev <= 3*mid:
            return True

        prev = num

    # print(s1, s2)
    return s1 + s2 <= 2*mid

    



def main():
    n = int(input())
    nums =  list(map(int, input().split()))

    # if nums.count(1)

    print(bs(1, 2**32, lambda x: check(x, nums)))
    




# Set the stack size
threading.stack_size(1 << 27)

# Create and start the main thread
main_thread = threading.Thread(target=main)
main_thread.start()

# Wait for the main thread to complete
main_thread.join()

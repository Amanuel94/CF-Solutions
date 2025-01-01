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
        m = int(input())
        a =  list(map(int, input().split()))
        b =  list(map(int, input().split()))
        
        sum_a = sum(a)
        sum_b = sum(b)

        and_sum =  sum([1 for i in range(m) if a[i] == 1 and b[i] == 1])
        if and_sum == min(sum_a, sum_b):
            print(abs(sum_a - sum_b))
        else:
            print(abs(sum_a - sum_b) + 1)
    




# Set the stack size
threading.stack_size(1 << 27)

# Create and start the main thread
main_thread = threading.Thread(target=main)
main_thread.start()

# Wait for the main thread to complete
main_thread.join()

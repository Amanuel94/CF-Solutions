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

# 2 1 2 1 1
# 2 1 2 2 
def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        nums =  list(map(int, input().split()))
        turn = 1
        for num in nums + [1]:
            if num != 1:
                break
            turn  = 1 - turn
            # print(num, turn)
        # print(turn)
        print("First") if turn else print("Second")
    




# Set the stack size
threading.stack_size(1 << 27)

# Create and start the main thread
main_thread = threading.Thread(target=main)
main_thread.start()

# Wait for the main thread to complete
main_thread.join()

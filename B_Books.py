import sys, threading
input = sys.stdin.readline
from collections import defaultdict
input = sys.stdin.readline

def main():
    n, t =  list(map(int, input().split()))
    nums = list(map(int, input().split()))
    cur = 0
    m = 0
    l = 0
    for r in range(n):
        cur+=nums[r]
        while cur > t:
            cur-=nums[l]
            l+=1
        m = max(m, r - l +1)
    print(m)
            

        
    




# Set the stack size
threading.stack_size(1 << 27)

# Create and start the main thread
main_thread = threading.Thread(target=main)
main_thread.start()

# Wait for the main thread to complete
main_thread.join()

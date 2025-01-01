import sys, threading
input = sys.stdin.readline
from collections import defaultdict
input = sys.stdin.readline
from heapq import heapify, heappush, heappop

def main():
    n = int(input())
    nums =  list(map(int, input().split()))
    max_ = float('-inf')
    heap = []
    i = 0
    while i < n:
        num = nums[i]
        if not heap or -heap[0] < num:
            heappush(heap, -num)
            max_ = max(max_, len(heap))
            i+=1
        else:
            heappop(heap)

    heap = []
    i = n-1
    while i > -1:
        num = nums[i]
        if not heap or heap[0] > num:
            heappush(heap, num)
            max_ = max(max_, len(heap))
            i-=1
        else:
            heappop(heap)
            
    print(max_)
    




# Set the stack size
threading.stack_size(1 << 27)

# Create and start the main thread
main_thread = threading.Thread(target=main)
main_thread.start()

# Wait for the main thread to complete
main_thread.join()

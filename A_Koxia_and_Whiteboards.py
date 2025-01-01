import sys
from heapq import heapify, heappop, heappush
input = sys.stdin.readline
from collections import defaultdict

t = int(input())
for _ in range(t):
    n, m = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    heapify(a)
    for bi in b:
        heappop(a)
        heappush(a, bi)
    print(sum(a))


"""
import sys, threading
sys.setrecursionlimit(10*3)
input = sys.stdin.readline

def main():
    

    # Set the stack size
threading.stack_size(1 << 27)

    # Create and start the main thread
main_thread = threading.Thread(target=main)
main_thread.start()

    # Wait for the main thread to complete
main_thread.join()


    



"""

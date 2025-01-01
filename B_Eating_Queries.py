from bisect import bisect_left
import sys, threading
input = sys.stdin.readline
from collections import defaultdict


def main():
    t = int(input())
    for __ in range(t):
        n, q =  list(map(int, input().split()))
        a = list(map(int, input().split()))
        a.sort(reverse=True)
        for _ in range(1, n):
            a[_] = a[_]+a[_-1]
        for _ in range(q):
            qi = int(input())
            if qi > a[-1]:
                print(-1)
            else:
                print(bisect_left(a, qi)+1)


    




# Set the stack size
threading.stack_size(1 << 27)

# Create and start the main thread
main_thread = threading.Thread(target=main)
main_thread.start()

# Wait for the main thread to complete
main_thread.join()

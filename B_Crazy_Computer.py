import sys, threading
input = sys.stdin.readline
from collections import defaultdict
input = sys.stdin.readline

def main():
    n, c=  list(map(int, input().split()))
    t = list(map(int, input().split()))
    cur = 1
    for i in range(1, n):
        cur = cur*int(t[i]-t[i-1]<=c)*1 + 1
    print(cur)
    




# Set the stack size
threading.stack_size(1 << 27)

# Create and start the main thread
main_thread = threading.Thread(target=main)
main_thread.start()

# Wait for the main thread to complete
main_thread.join()

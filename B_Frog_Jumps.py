import sys, threading
input = sys.stdin.readline
from collections import defaultdict
input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        s =  input().strip()
        s =  s + 'R'
        max_gap = 1
        last_R = -1
        for i, c in enumerate(s):
            if c == "R":
                max_gap = max(max_gap, i - last_R)
                last_R = i
        print(max_gap)

    




# Set the stack size
threading.stack_size(1 << 27)

# Create and start the main thread
main_thread = threading.Thread(target=main)
main_thread.start()

# Wait for the main thread to complete
main_thread.join()


import sys, threading
input = sys.stdin.readline
from collections import defaultdict
input = sys.stdin.readline

def main():
    v1, v2 =  list(map(int, input().split()))
    t, d = list(map(int, input().split()))
    path = v1
    v = v1
    while v < v2:
        v+=d
        path+=v
        t-=1
    c = d
    while c > 0:
        if (v+c-v2)//d <= t:
            v+=c
            path+=v
            t-=1
        elif c > 0:
            c-=1
    while


    

    # t > [b - v2]//d
    # dp[ti]
    




# Set the stack size
threading.stack_size(1 << 27)

# Create and start the main thread
main_thread = threading.Thread(target=main)
main_thread.start()

# Wait for the main thread to complete
main_thread.join()

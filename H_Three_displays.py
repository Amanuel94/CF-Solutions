"""
2   4   5   4   10
inf 70  50  50  50
inf inf 90  inf 90
"""
import sys, threading
input = sys.stdin.readline
from collections import defaultdict
input = sys.stdin.readline

def main():
    n = int(input())
    s =  list(map(int, input().split()))
    c =  list(map(int, input().split()))

    second = [float('inf')]*n
    third = [float('inf')]*n

    # second[i] = min(second[i], cost[i]+cost[tj]) s[tj] < s[i]
    for i in range(n):
        for j in range(i-1, -1, -1):
            if s[i] > s[j]:
                second[i] = min(second[i], c[i]+c[j])
    for i in range(n):
        for j in range(i-1, -1, -1):
            if s[i] > s[j]:
                third[i] = min(third[i], c[i]+second[j])
    ans = min(third)
    if ans == float('inf'):
        print(-1)
    else:
        print(ans)


    




# Set the stack size
threading.stack_size(1 << 27)

# Create and start the main thread
main_thread = threading.Thread(target=main)
main_thread.start()

# Wait for the main thread to complete
main_thread.join()


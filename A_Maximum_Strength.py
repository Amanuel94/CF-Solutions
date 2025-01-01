import sys, threading
input = sys.stdin.readline
from collections import defaultdict
inf = float('inf')
MOD = 10**9 + 7
# returns the first number where key becomes true for a given delegate type key
def bs(low=1, high=1, key = lambda x: True):

    while low <= high:
        mid = (low + high)//2
        if key(mid):
            high = mid-1
        else:
            low = mid+1
    return low
# 199
# 200
# 53 57
def main():
    t = int(input())
    for _ in range(t):
        L, R = input().strip().split()
        L = (len(R) - len(L))*"0" + L
        i = 0
        while i < len(R) and R[i] == L[i]:
            i+=1
        if i < len(R):
            print(9*(len(L)-i-1) + int(R[i]) - int(L[i]))
        else:
            print(0)
      




# Set the stack size
threading.stack_size(1 << 27)

# Create and start the main thread
main_thread = threading.Thread(target=main)
main_thread.start()

# Wait for the main thread to complete
main_thread.join()

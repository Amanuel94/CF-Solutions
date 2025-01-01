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


def main():
    t = int(input())
    for _ in range(t):
        n,m, k, H =  list(map(int, input().split()))
        h =  list(map(int, input().split()))
        ans = 0
        for hi in h:
            if abs(H - hi)%k == 0 and 1 <= abs(H - hi) <= (m-1)*k:
                # print(hi, end = "-.")
                ans +=1
        print(ans)
    




# Set the stack size
threading.stack_size(1 << 27)

# Create and start the main thread
main_thread = threading.Thread(target=main)
main_thread.start()

# Wait for the main thread to complete
main_thread.join()

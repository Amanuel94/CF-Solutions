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


def main():
    t = int(input())
    for _ in range(t):
        s = input().strip()
        l, r = 0, len(s)-1
        ans = [""]*len(s)
        look = ["0", "1"]
        while l <= r:
            while l <= r and s[l] != look[1]:
                ans[l] = look[0]
                l+=1
            
            while l <= r and s[r] != look[0]:
                ans[r] = look[1]
                r-=1
            
            look[0], look[1] = look[1], look[0]
        print("".join(ans))


    




# Set the stack size
threading.stack_size(1 << 27)

# Create and start the main thread
main_thread = threading.Thread(target=main)
main_thread.start()

# Wait for the main thread to complete
main_thread.join()

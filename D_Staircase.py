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
        n = int(input())
        a =  list(map(int, input().split()))
        # s, m = 2*sum(a), max(a)
        # if n % 2:
        #     s -= m
        # print(s)
        ans = 0
        prefix = 0
        running_max = 0
        l = r =  0
        while r < n:
            if a[r] > 0:
                prefix += 2*a[r]
                if (r - l) % 2 == 0:
                    running_max = max(running_max, a[r])
            else:
                if (r - l)%2:
                    prefix -= running_max
                ans += prefix
                prefix = 0
                running_max = 0
                l = r + 1
            r+=1
                
        if (r - l)%2:
            prefix -= running_max
        ans += prefix
        print(ans)


    




# Set the stack size
threading.stack_size(1 << 27)

# Create and start the main thread
main_thread = threading.Thread(target=main)
main_thread.start()

# Wait for the main thread to complete
main_thread.join()

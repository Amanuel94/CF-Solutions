import sys, threading
input = sys.stdin.readline
from collections import defaultdict
inf = float('inf')
MOD = 10**9 + 7
# returns the first number where key becomes true for a given delegate type key
# 1 4 2 3 
# 1110101011
# 0101011111
# 0010111111
# 0000111111
# 001110110
# 
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
        i = 0
        j = n-1
        ans = []
        while i <= j:
            ans.append(i+1)
            ans.append(j+1)
            i+=1
            j-=1
        if n > 1 and ans[-1] == ans[-2]: ans.pop()
        print(*ans)


    




# Set the stack size
threading.stack_size(1 << 27)

# Create and start the main thread
main_thread = threading.Thread(target=main)
main_thread.start()

# Wait for the main thread to complete
main_thread.join()

import sys, threading
input = sys.stdin.readline
from collections import Counter, defaultdict
inf = float('inf')
MOD = 10**9 + 7
# returns the first number where key becomes true for a given delegate type key
# 111100
# 001111
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
        c = Counter(s)
        count = 0
        i = 0
        for si in s:
            a = "1" if si == "0" else "0"
            if c[a] > 0:
                c[a]-=1
                i+=1
            else:
                break
                
        print(len(s) - i)
            


    




# Set the stack size
threading.stack_size(1 << 27)

# Create and start the main thread
main_thread = threading.Thread(target=main)
main_thread.start()

# Wait for the main thread to complete
main_thread.join()

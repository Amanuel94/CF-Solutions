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
        n, k = list(map(int, input().split()))
        a =  list(map(int, input().split()))
        m = -1
        
        if k in [2, 3, 5]:
            for ai in a:
                if ai%k == 0:
                    m = k
                    break
                m = max(ai%k, m)
            print(k - m)
        else:
            c = 0
            d = 0

            for ai in a:
                if ai%2 == 0:
                    c+=1
                if ai%4 == 0:
                    print(0)
                    break
                m = max(ai%4, m)
                if c > 1:
                    print(0)
                    break
            else:
                print(min(max(0, 2 - c), 4 - m))

            
            
    




# Set the stack size
threading.stack_size(1 << 27)

# Create and start the main thread
main_thread = threading.Thread(target=main)
main_thread.start()

# Wait for the main thread to complete
main_thread.join()

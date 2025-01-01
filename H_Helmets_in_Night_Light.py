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
        n, c =  list(map(int, input().split()))
        a = [n] + list(map(int, input().split()))
        b = [c] + list(map(int, input().split()))
        ab = list(zip(a, b))
        ab.sort(key = lambda x: x[1])
        cost = c
        heard = 1
        for su, c in ab:
            if heard >= n:
                print(cost)
                break
            cost += c*min(n - heard, su)
            heard += su
        
            




# Set the stack size
threading.stack_size(1 << 27)

# Create and start the main thread
main_thread = threading.Thread(target=main)
main_thread.start()

# Wait for the main thread to complete
main_thread.join()

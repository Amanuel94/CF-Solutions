import math
import sys, threading
input = sys.stdin.readline
from collections import defaultdict
inf = float('inf')
MOD = 10**9 + 7
# returns the first number where key becomes true for a given delegate type key
# 50 25 10 5 2 
def bs(low=1, high=1, key = lambda x: True):

    while low <= high:
        mid = (low + high)//2
        if key(mid):
            high = mid-1
        else:
            low = mid+1
    return low

# a b x 
def main():
    t = int(input())
    for _ in range(t):
        a, b =  list(map(int, input().split()))
        if a == 1:
            print(b*b)
            continue
        lcm = (a*b)//math.gcd(a, b)
        if b%a == 0:
            # g = math.gcd(a, b)
            d = 2
            while d*d <= lcm and lcm%d !=0:
                d+=1
            print(lcm*d)

        else:
            print(lcm)

    




# Set the stack size
threading.stack_size(1 << 27)

# Create and start the main thread
main_thread = threading.Thread(target=main)
main_thread.start()

# Wait for the main thread to complete
main_thread.join()

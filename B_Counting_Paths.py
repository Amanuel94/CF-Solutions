import sys, threading
input = sys.stdin.readline
from collections import defaultdict
input = sys.stdin.readline
import math
N = pow(10, 9) + 7

"""
    a   b   f(a, b) 
    0   0   2
    1   0   2       l r
    2   0   2       ll rr
    2   1   2       lr rl
    3               lll rrr 
                    llr lrr rll rrl 3 1
                    lrl rlr
    n... n-k+1
    
    
 """

def main():
    t = int(input())
    memo = defaultdict(int)
    def dp(a, b):

            if (a <= b):
                return 0
            if b == 0:
                 return 2
            
            if (a, b) in memo:
                return memo[(a,b)]%N
            memo[(a,b)] = (dp(a-1, b) + dp(a-1, b-1))%N
            return memo[(a,b)]%N
    for _ in range(t):
        a, b = list(map(int, input().split()))
        # memo = defaultdict(int)
        print(dp(a,b))
             

    




# Set the stack size
threading.stack_size(1 << 27)

# Create and start the main thread
main_thread = threading.Thread(target=main)
main_thread.start()

# Wait for the main thread to complete
main_thread.join()

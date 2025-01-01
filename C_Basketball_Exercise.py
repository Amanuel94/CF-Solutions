
import sys
import threading
input = sys.stdin.readline
from collections import defaultdict
input = sys.stdin.readline

def main():
        

    n = int(input())
    t1 = list(map(int, input().split()))
    t2 = list(map(int, input().split()))

    t = [t1, t2]

    memo = defaultdict(int)
    def dp(p, f):
        if p == -1:
            return 0
        elif (p, f) in memo:
            return memo[(p, f)]
        else:
            memo[(p,f)] = 0
            memo[(p,f)] =  max(dp(p-1,1-f)+t[f][p], dp(p-1,f))
            return memo[(p,f)]
        
    print(max(dp(n-1, 1), dp(n-1, 0)))
        


    

# Set the stack size
threading.stack_size(1 << 27)

# Create and start the main thread
main_thread = threading.Thread(target=main)
main_thread.start()

# Wait for the main thread to complete
main_thread.join()

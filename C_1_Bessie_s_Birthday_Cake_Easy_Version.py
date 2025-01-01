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
        n, x, y =  list(map(int, input().split()))
        xs = list(map(int, input().split()))
        xs.sort()
        if x == 1:
            print(0)
            continue
            
        if x == 2:
            if(xs[1])%n == (xs[0]+2)%n or (xs[0])%n == (xs[-1]+2)%n :
                print(2) if n == 4 else print(1)
                continue
            else:
                print(0)
                continue
        cons = 0
        for i in range(x):
            if (xs[i])%n == (xs[i-1]+2)%n:
                
                cons+=1
        # print(cons)        
        
        print(x-2 + cons)
    




# Set the stack size
threading.stack_size(1 << 27)

# Create and start the main thread
main_thread = threading.Thread(target=main)
main_thread.start()

# Wait for the main thread to complete
main_thread.join()

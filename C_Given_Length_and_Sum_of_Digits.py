from functools import cache
import sys, threading
input = sys.stdin.readline
from collections import defaultdict
input = sys.stdin.readline

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
    m,s =  list(map(int, input().split()))
    if m > 1 and s == 0:
        print(-1, -1)
        exit(0)
    if s > m*9:
        print(-1, -1)
        exit(0)
    if m == 1 and s == 0:
        print(0,0)
        exit(0)
    
    max_num = [0]*m
    i = 0
    while i < m:
        for j in range(9, -1,-1):
            if s - j >= 0:
                max_num[i] = j
                s-=j
                break
        else:
            print(-1,-1)
            break
        i+=1

    min_num = [0]*m
    i = m-1
    while i > -1 and max_num[i] == 0:
        i-=1
    if i < m-1:
        min_num[0] = 1
        min_num[m-1-i] = max_num[i]-1
        i-=1
    while i > -1:
        min_num[m-1-i] = max_num[i]
        i-=1

    print("".join(map(str, min_num)), end = " ")
    print("".join(map(str, max_num)))
        

    




        

        
        
    




# Set the stack size
threading.stack_size(1 << 27)

# Create and start the main thread
main_thread = threading.Thread(target=main)
main_thread.start()

# Wait for the main thread to complete
main_thread.join()

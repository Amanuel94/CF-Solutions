import sys, threading
input = sys.stdin.readline
from collections import defaultdict
inf = float('inf')
MOD = 10**9 + 7

def si():
    return input()
def ii():
    return int(input())
def lsi():
    return input().split()
def mi():
    return map(int, input().split())
def li():
    return list(map(int, input().split()))

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
        n = ii()
        a = li()
        bwand = a[0]
        for ai in a:
            bwand&=ai
        if bwand > 0:
            print(1)
            continue
        cur = a[0]
        ans = 0
        i = 0
        while i < len(a):
            if cur < 0: cur = a[i]
            cur = cur & a[i]
            if cur == 0:
                ans+=1
                cur = -1
            i+=1
        
        print(ans)


    
    




# Set the stack size
threading.stack_size(1 << 27)

# Create and start the main thread
main_thread = threading.Thread(target=main)
main_thread.start()

# Wait for the main thread to complete
main_thread.join()

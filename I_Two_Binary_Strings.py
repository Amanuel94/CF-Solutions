import sys, threading
input = sys.stdin.readline
from collections import defaultdict
inf = float('inf')
MOD = 10**9 + 7

def si():
    return input().strip()
def ii():
    return int(input())
def lsi():
    return input().strip().split()
def mi():
    return map(int, input().split())
def li():
    return list(map(int, input().split()))
# 0 1 1
# 0 - -
# 0 1 -
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
    t = ii()
    for _ in range(t):
        a = si()
        b = si()
        if a == b:
            print("YES")
            continue
      
        az = [-1]*len(a)
        bz = [-1]*len(b)
        for i in range(len(a)-2, -1, -1):
            if a[i] == "0": az[i] = i
            else: az[i] = az[i+1]
            if b[i] == "0": bz[i] = i
            else: bz[i] = bz[i+1]
        
        i = 0
        f = 0
        # print(az, bz)
        while i < len(a):
            if a[i] == b[i]:
                if a[i] == "0":
                    i+=1
                else: 
                    print("YES") 
                    f = 1
                    break
            else:
                if az[i] == -1 or bz[i] == -1: 
                    print("NO")
                    f = 1
                    break
                i = max(az[i], bz[i])
        if not f: print("NO")

            
        
            





            
        
    
    




# Set the stack size
threading.stack_size(1 << 27)

# Create and start the main thread
main_thread = threading.Thread(target=main)
main_thread.start()

# Wait for the main thread to complete
main_thread.join()

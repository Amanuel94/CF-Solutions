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
# 2 1   1
# 4 3   2
# 8 7                       
# n n, n//2 + 1, n//3 + 2, n//4 + 3   N//x + x - 2
# + 1
# LEN
# 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 7 7 7 7 7 7
# 1 2 3 6 7 
# 1 -> 2 -> 2 2 -> 2 3
# 1 -> 2 -> 2 2-> 2 2 2
# 

def rec(n):
    if n == 1: return 0
    fac = [1, n]
    d = 2
    while d*d <= n:
        if n%d == 0:
            fac.append(d)
            if d != n//d:
                fac.append(n//d)
        d+=1
    ans = inf
    for d in fac:
        ans = min(d - 1 + n//d - 1, ans)
    al = inf
    if len(fac) == 2:
        al = rec(n-1) + 1
    return min(ans, al)


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(rec(n))
    




# Set the stack size
threading.stack_size(1 << 27)

# Create and start the main thread
main_thread = threading.Thread(target=main)
main_thread.start()

# Wait for the main thread to complete
main_thread.join()

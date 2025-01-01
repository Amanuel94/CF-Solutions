import sys, threading
input = sys.stdin.readline
from collections import Counter, defaultdict
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
        n, m, k =  list(map(int, input().split()))
        a =  list(map(int, input().split()))
        b =  list(map(int, input().split()))
        ca =  set(a)
        cb = set(b)

        # i = k//2
        # j = k//2
       

        # while  
        ai = k//2
        bi = k//2 
       
        for i in range(1, k+1):
            if i not in ca and i in cb:
                bi-=1
            if i  in ca and i not in cb:
                ai-=1
            if i not in ca and i not in cb:
                print("NO")
                break
        else:
            if ai > -1 and bi > -1:
                print("YES")
            else:
                print("NO")
            

main()

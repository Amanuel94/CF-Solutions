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
        n = int(input())
        grid = []
        for __ in range(n):
            grid.append(list(map(int , list(input().strip()))))
        
        
        ans = 0
        i = 0
        while n - 2*i > 1:
            for j in range(i, n-i-1):
                ones = 0
                ii, jj = i, j
                for k in range(4):
                    ones += grid[ii][jj]
                    # print(ii, jj)
                    ii, jj = jj, n - 1 - ii

                ans += min(ones, 4 - ones)
            i+=1
        print(ans)

            

            
    
main()
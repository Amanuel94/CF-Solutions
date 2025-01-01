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
    t = int(input())
    for _ in range(t):

        n = int(input())
        if n <= 6 or (n%3 == 0 and n//3 % 3 == 0):
            print("NO")
            continue
        print("YES")
        print(*[n//3-((-n//3)%3) , n//3, n//3+(n//3)%3])

main()

 
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
    n = int(input())
    a =  list(map(int, input().split()))
    b = list(map(int, input().split()))

    row1 = [0]*n
    row2 = [0]*n

    row1[0] = a[0]
    row2[0] = b[0]

    for i in range(1, n):
        row1[i] = max(row2[i-1], row1[i-1]-a[i-1]) +a[i]
        row2[i] = max(row1[i-1], row2[i-1]-b[i-1]) +b[i]
    print(max(row1[-1], row2[-1]))



    




main()

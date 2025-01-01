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
    queries = defaultdict(str)
    for _ in range(t):
        o, n = input().strip().split()
        for key in queries:
            if queries[key] == o:
                queries[key] = n
                break
        else:
            queries[o] = n

    print(len(queries))
    for key in queries:
        print(key, queries[key])

main()

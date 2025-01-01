import sys, threading
input = sys.stdin.readline
from collections import defaultdict
input = sys.stdin.readline

def main():
    t = int(input())
    nums =  list(map(int, input().split()))
    print(*sorted(nums))
    


main()
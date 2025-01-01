import sys, threading
input = sys.stdin.readline
from collections import defaultdict
input = sys.stdin.readline

def main():
    s1 = input().strip()
    s2 = input().strip()

    if s1 == s2:
        print(-1)
    else:
        print(max(len(s1), len(s2)))
    


main()

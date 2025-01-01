import sys, threading
input = sys.stdin.readline
from collections import defaultdict
input = sys.stdin.readline
from bisect import bisect_left, bisect_right

"""
2 9 1 3 18 1 4

2 11 12 15 20 33 34 38

"""
def main():
    t = int(input())
    for _ in range(t):
        n, s = list(map(int, input().split()))
        a = list(map(int, input().split()))
        b = a[:]
        for i in range(1, n):
            a[i]+=a[i-1]
        if a[-1] <= s:
            print(0)
            continue
        max_ = float('-inf')
        ans = 0
        for i, ai in enumerate(b):
            
            ind = bisect_right(a, ai+s)
            # print(a, ai+s, ind, i)
            if max_ < ind and a[i]-ai <= s:
                max_ = ind
                ans = i+1
        print(ans)   
                    
        
    




# Set the stack size
threading.stack_size(1 << 27)

# Create and start the main thread
main_thread = threading.Thread(target=main)
main_thread.start()

# Wait for the main thread to complete
main_thread.join()

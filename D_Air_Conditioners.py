
import sys, threading
input = sys.stdin.readline
from collections import defaultdict
input = sys.stdin.readline

def main():
    T = int(input())
    for _ in range(T):
        input()
        n,k = list(map(int, input().split()))
        a  = list(map(int, input().split()))
        t = list(map(int, input().split()))
        l = [float('inf')]*n
        r = [float('inf')]*n

        for i, ai in enumerate(a):
            l[ai-1] = t[i]
            r[ai-1] = t[i]
        


        i = 1
        while i < n:
            r[i] = min(r[i-1]+1, r[i])
            l[n-1-i] = min(l[n-i]+1, l[n-i-1])
            i+=1
        i = 0
        while i < n:
            print(min(l[i], r[i]), end = " ")
            i+=1
        print()
       
    
    




# Set the stack size
threading.stack_size(1 << 27)

# Create and start the main thread
main_thread = threading.Thread(target=main)
main_thread.start()

# Wait for the main thread to complete
main_thread.join()

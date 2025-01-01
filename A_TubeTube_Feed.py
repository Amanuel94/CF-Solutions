import sys
import threading
input = sys.stdin.readline
from collections import defaultdict
input = sys.stdin.readline

def main():
    q = int(input())
    for _ in range(q):
        n, t = list(map(int, input().split()))
        a =  list(map(int, input().split()))
        b = list(map(int, input().split()) )

        ans = -1
        max_ = float('-inf')

        i = 0

        while i < n and t:
            if a[i] <= t:
                if b[i] > max_:
                    ans = (i+1)
                    max_ = b[i]
            t-=1
            i+=1
        print(ans)


        




# Set the stack size
threading.stack_size(1 << 27)

# Create and start the main thread
main_thread = threading.Thread(target=main)
main_thread.start()

# Wait for the main thread to complete
main_thread.join()

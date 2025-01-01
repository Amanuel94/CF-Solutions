
import sys
import threading
input = sys.stdin.readline
from collections import defaultdict
input = sys.stdin.readline

def main():
        n, k = list(map(int, input().split()))
        p =  list(map(int, input().split()))
        s = sum(p[:k])

        ans = -1
        min_ = float('inf')

        i = 0
        # print(s)
        while i < n-k:
            if s < min_:
                ans = i
                min_ = s
            s+=(p[i+k] - p[i])
            i+=1

        if s < min_:
            ans = i
            min_ = s
        
        if ans == -1:
             print(1)
        else: 
            print(ans+1)


        




# Set the stack size
threading.stack_size(1 << 27)

# Create and start the main thread
main_thread = threading.Thread(target=main)
main_thread.start()

# Wait for the main thread to complete
main_thread.join()

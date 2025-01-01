import sys, threading
input = sys.stdin.readline
from collections import defaultdict
input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        nums =  list(map(int, input().split()))
        nums.sort(reverse=True)
        ans = 0
        for s in range(1, 8):
            f = True
            for k in range(3):
                if (s>>k)&1 and nums[k] == 0:
                    f = False
            if f:
                ans+=1
                for k in range(3):
                    if (s>>k)&1:
                        nums[k]-=1
        print(ans)
                    
        
    




# Set the stack size
threading.stack_size(1 << 27)

# Create and start the main thread
main_thread = threading.Thread(target=main)
main_thread.start()

# Wait for the main thread to complete
main_thread.join()

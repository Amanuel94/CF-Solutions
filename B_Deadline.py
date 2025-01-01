import sys, threading
input = sys.stdin.readline
from collections import defaultdict
input = sys.stdin.readline
import math
def main():
    t = int(input())
    for _ in range(t):
        n, d =  list(map(int, input().split()))
        # sm = math.ceil(d/(n))-1
        # if(sm + math.ceil(d/(sm+1)) <= n):
        #     print("YES")
        # else:
        #     print("NO")

        for x in range(n-1, -1 ,-1):
            # print(x)
            if((x + math.ceil(d/(x+1))) <= n):
                print("YES")
                break
        else:
            print("NO")


        
    




# Set the stack size
threading.stack_size(1 << 27)

# Create and start the main thread
main_thread = threading.Thread(target=main)
main_thread.start()

# Wait for the main thread to complete
main_thread.join()

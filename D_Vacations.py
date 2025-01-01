
import sys
import threading
input = sys.stdin.readline
from collections import defaultdict
input = sys.stdin.readline

def main():
        

    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    e = 0

    for ai in a:
        # print(ai, e)
        if ai == 0:
            ans+=1
            e = 0
        elif e == 0:
            if ai == 1:
                e = 2
            elif ai == 2:
                e = 1
        elif ai!=3:
            if e != ai:
                ans+=1
                e = 0
            else:
                e = 2 if e == 1 else 1
# 
        else:
            e = 2 if e == 1 else 1
    print(ans)


# Set the stack size
threading.stack_size(1 << 27)

# Create and start the main thread
main_thread = threading.Thread(target=main)
main_thread.start()

# Wait for the main thread to complete
main_thread.join()

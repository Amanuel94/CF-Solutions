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
    in_map = {}
    t = int(input())
    count = 0
    cap = 0
    for _ in range(t):
        # print(count)
        op, id = input().strip().split()
        if op == "+":
            in_map[id] = False
            if cap:
                cap-=1
            else:
                count+=1
        else:
            if id in in_map:
                del in_map[id]
            else:
                count+=1
            cap+=1
    print(count)

        
    




# Set the stack size
threading.stack_size(1 << 27)

# Create and start the main thread
main_thread = threading.Thread(target=main)
main_thread.start()

# Wait for the main thread to complete
main_thread.join()

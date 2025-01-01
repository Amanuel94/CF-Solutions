import sys, threading
input = sys.stdin.readline
from collections import defaultdict
inf = float('inf')
# returns the first number where key becomes true for a given delegate type key
#  +++-----
def bs(low=1, high=1, key = lambda x: True):

    while low <= high:
        mid = (low + high)//2
        if key(mid):
            high = mid-1
        else:
            low = mid+1
    return low


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        s =  input()
        quan = [0]*(n+1)
        for i in range(n):
            if s[i] == "-":
                quan[i+1] = quan[i] + 1
            else:
                quan[i+1] = quan[i] - 1
        count = 0
        
        m = {}
        # qj - qi mod 3 = 0
        for q in quan:
            count += m.get((q)%3, 0)
            if (q)%3 not in m:
                m[(q)%3] = 0
            m[(q)%3] += 1
               
        print(count)
                    




# Set the stack size
threading.stack_size(1 << 27)

# Create and start the main thread
main_thread = threading.Thread(target=main)
main_thread.start()

# Wait for the main thread to complete
main_thread.join()

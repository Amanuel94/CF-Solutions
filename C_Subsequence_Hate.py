import sys, threading
input = sys.stdin.readline
from collections import defaultdict
input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        s = list(input().strip())
        L = 0
        R = sum(map(int, s))
        ans = R
        for si in s:
            if si == '0':
                L+=1
            else:
                R-=1
            ans = min(ans, L+R)
        # print(ans)

        s.reverse()
        L = 0
        R = sum(map(int, s))
        ans1 = R
        for si in s:
            if si == '0':
                L+=1
            else:
                R-=1
            ans1 = min(ans1, L+R)
        print(min(ans, ans1))


    
    




# Set the stack size
threading.stack_size(1 << 27)

# Create and start the main thread
main_thread = threading.Thread(target=main)
main_thread.start()

# Wait for the main thread to complete
main_thread.join()

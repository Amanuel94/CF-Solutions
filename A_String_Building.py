import sys, threading
input = sys.stdin.readline
from collections import defaultdict
input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        s = input().strip()
        if len(s) == 1:
            print("NO")
            continue
        for i in range(1, len(s)-1):
            if s[i-1] == s[i+1] and s[i] != s[i-1]:
                print("NO")
                break
        else:
            if(s[0]!= s[1] or s[-1]!= s[-2]):
                print("NO")
            else:
                print("YES")
    




# Set the stack size
threading.stack_size(1 << 27)

# Create and start the main thread
main_thread = threading.Thread(target=main)
main_thread.start()

# Wait for the main thread to complete
main_thread.join()

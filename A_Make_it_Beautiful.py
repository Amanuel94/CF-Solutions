import sys, threading
input = sys.stdin.readline
from collections import defaultdict
input = sys.stdin.readline

def main():
    t = int(input())

    for _ in range(t):
        n = int(input())
        a =  list(map(int, input().split()))
        a.sort(reverse=True)
        if a[0] == a[1]:
            i = 0
            while i < len(a) and a[i]== a[0]:
                i+=1
            if i == n:
                print("NO")
            else:
                a[1],a[i] = a[i],a[1]
                print("YES")
                print(*a)
        else:
            print("YES")
            print(*a)
    




# Set the stack size
threading.stack_size(1 << 27)

# Create and start the main thread
main_thread = threading.Thread(target=main)
main_thread.start()

# Wait for the main thread to complete
main_thread.join()

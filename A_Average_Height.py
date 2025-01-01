import sys, threading
input = sys.stdin.readline
from collections import defaultdict
input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a =  list(map(int, input().split()))
        odds = []
        evens = []
        for i in range(n):
            if a[i]%2:
                odds.append(a[i])
            else:
                evens.append(a[i])
        odds.extend(evens)
        print(*(odds))


    




# Set the stack size
threading.stack_size(1 << 27)

# Create and start the main thread
main_thread = threading.Thread(target=main)
main_thread.start()

# Wait for the main thread to complete
main_thread.join()

import sys, threading
input = sys.stdin.readline
from collections import defaultdict
input = sys.stdin.readline

def main():
    s = input().strip()
    # A = set()
    # B = set()
    n= len(s)
    cur = None
    found = []
    look_for = ["AB", "BA"]
    last_AB = []
    last_BA = []
    for i in range(n-1):
        if s[i]+s[i+1] in "AB":
            last_AB.append(i)
            if last_BA and last_BA[0] != i-1:
                print("YES")
                break
        elif s[i]+s[i+1] in "BA":
            last_BA.append(i)
            if last_AB and last_AB[0] != i-1:
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

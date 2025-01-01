import sys, threading
input = sys.stdin.readline
from collections import defaultdict
input = sys.stdin.readline

def main():
    d = defaultdict(int)
    for _ in range(3):
        
        s = input().strip()
        if s[1] == '>':
            d[s[0]]+=1
        else:
            d[s[2]]+=1

    r = sorted(['A', 'B', 'C'], key = lambda x:d[x])
    ans = ""
    c = 0
    for a in r:
        if d[a] == c:
            c+=1
            ans+=a
        else:
            print("Impossible")
            break
    else:
        print(ans)

    




# Set the stack size
threading.stack_size(1 << 27)

# Create and start the main thread
main_thread = threading.Thread(target=main)
main_thread.start()

# Wait for the main thread to complete
main_thread.join()

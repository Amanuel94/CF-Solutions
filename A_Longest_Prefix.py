import sys, threading
input = sys.stdin.readline
from collections import defaultdict, Counter
input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        a, b = input().split()
        a = list(a.strip())
        b = list(b.strip())
        
        c =  dict(Counter(b))
        ans = 0
        for ai in a:
            if ai in c and c[ai]>0:
                c[ai]-=1
                ans+=1 
            else:
                break 
        print(ans)


            
            
            


    




# Set the stack size
threading.stack_size(1 << 27)

# Create and start the main thread
main_thread = threading.Thread(target=main)
main_thread.start()

# Wait for the main thread to complete
main_thread.join()

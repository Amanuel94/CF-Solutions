
import sys
import threading
input = sys.stdin.readline
from collections import defaultdict
input = sys.stdin.readline

def main():
        
        l = 0 
        r = 0 
        s = input().strip()
        s+=('a')
        for c in s:
            if c.isupper():
                r+=1
        ans = float('inf')
        for c in s:
            ans = min(l+r, ans)
            if c.islower():
                l+=1
            else:
                r-=1
        print(ans)
            
            
                 

        




# Set the stack size
threading.stack_size(1 << 27)

# Create and start the main thread
main_thread = threading.Thread(target=main)
main_thread.start()

# Wait for the main thread to complete
main_thread.join()

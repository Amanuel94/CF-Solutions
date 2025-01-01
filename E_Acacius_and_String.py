import sys, threading
input = sys.stdin.readline
from collections import defaultdict
inf = float('inf')
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
    t = int(input())
    for _ in range(t):
        n  = int(input())
        s = input().strip()
        r = "abacaba"

        def eq(i):
            nonlocal s, r
            cur = 3
            j = 1
            while j <=3 and i + j < len(s) and i - j > -1:
                if s[i+j] != "?" and s[i+j] != r[cur+j]:
                    return False, False
                if s[i-j] != "?" and s[i-j] != r[cur - j]:
                    return False, False
                j+=1

            q = False
            if j == 4:
                for k in range(max(0,i-3), min(i+4, len(s))):
                    if s[k] == '?':
                        q = True
                        break

            return j == 4, q
        
        
        # print(eq(3))
        counter = 0
        last = -1
        for i in range(n):
            if s[i] in "c?":
                possible, q = eq(i)
                
                if possible:
                    if last == -1:
                        last = i
                    
                    if not q:
                        counter+=1
                        last = i
        

        if last == -1 or counter > 1:
           print("No")
        else:
            i = last
            print("Yes")
            k = s[:i-3] + r + s[i+4:]
            k = k.replace('?', 'z')
            print(k)
            
            

            


    




# Set the stack size
threading.stack_size(1 << 27)

# Create and start the main thread
main_thread = threading.Thread(target=main)
main_thread.start()

# Wait for the main thread to complete
main_thread.join()

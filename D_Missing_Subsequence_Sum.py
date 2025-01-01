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

# 1 2 1 2 8
# 1

p = {i:2**i for i in range(32)}

def main():

    def pref(n):
        ans = []
        i = 0
        while p[i] <= n:
            n-=p[i]
            ans.append(p[i])
            i+=1
        ans.append(n)
        return ans
            

    t = int(input())
    for _ in range(t):
        ans = []
        n, k =  list(map(int, input().split()))
        ans.extend(pref(k-1))
        if k < n:
            ans.append(k+1)
            ans.append(2*k + k+ 1)
            up = 2*k
            # 1 2 3 . . . k-1 k+1 
            while up < n:
                ans.append(up+1)
                
                up+=(up+1)
    
        while ans and ans[-1] > n:
            ans.pop()

        ans = [i for i in ans if i != 0]
        
        print(len(ans))
        print(*ans)


# Set the stack size
threading.stack_size(1 << 27)

# Create and start the main thread
main_thread = threading.Thread(target=main)
main_thread.start()

# Wait for the main thread to complete
main_thread.join()

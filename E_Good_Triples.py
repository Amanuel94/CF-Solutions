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

pre = defaultdict(int)
seen = set()
for i in range(10):
    for j in range(10):
        for k in range(10):
            if (i, j , k) not in seen:
                pre[i+j+k]+=1
                seen.add((i, j, k))



def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        ans = 1
        while n > 0:
            last = n%10
            n//=10
            ans *= pre[last]
        print(ans)




    




# Set the stack size
threading.stack_size(1 << 27)

# Create and start the main thread
main_thread = threading.Thread(target=main)
main_thread.start()

# Wait for the main thread to complete
main_thread.join()

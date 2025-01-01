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

        na, nb, k =  list(map(int, input().split()))
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        pairs = list(zip(a, b))
        pairs = list(set(pairs))
        countf =defaultdict(int)
        counts = defaultdict(int)
        for ai, bi in pairs:
            countf[ai]+=1
            counts[bi]+=1
        
        ansf = k*k
        for k in countf:
            ansf-=countf[k]*countf[k]
        ansf//=2
        
        for k in counts:
            cur = counts[k]
            ansf-=(cur*cur - cur)//2

        print(ansf)
            


    

            

    




# Set the stack size
threading.stack_size(1 << 27)

# Create and start the main thread
main_thread = threading.Thread(target=main)
main_thread.start()

# Wait for the main thread to complete
main_thread.join()

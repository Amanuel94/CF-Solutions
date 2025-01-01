from heapq import heapify, heappop, heappush
import sys, threading
input = sys.stdin.readline
from collections import defaultdict, Counter
input = sys.stdin.readline

def main():
    n, k =  list(map(int, input().split()))
    nums =  list(map(int, input().split()))
    c = list(Counter(nums).items())
    c.sort(key = lambda x: x[1], reverse=True)
    o = [x[1] for x in c]
    o = list(Counter(o).items())
    
    o = [(-x[1], x[0]) for x in o]
    # print(o)
    
    heapify(c)
    ans = []
    for _ in range(k):
        f, v = heappop(c)
        x, y = heappop(o)
        heappush(c, ((f-o[0][1], v)))
        x+=1
        if x < 0:
            heappush(o, (x,y))
        ans.append(v)
    print(*ans)


    
    




# Set the stack size
threading.stack_size(1 << 27)

# Create and start the main thread
main_thread = threading.Thread(target=main)
main_thread.start()

# Wait for the main thread to complete
main_thread.join()

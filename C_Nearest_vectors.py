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

def normalize(vecs):
    
    normalized = []
    for x, y in vecs:
        dist = (x**2 + y**2)**0.5      
        normalized.append((x/dist, y/dist))
    
    return normalized

def dot(a, b):
    return a[0]*b[0] + a[1]*b[1]






def main():
    t = int(input())
    vecs = []
    for _ in range(t):
        a, b =  list(map(int, input().split()))
        vecs.append((a, b))
    
    vecs = normalize(vecs)
    vecs = [(vecs[i], i) for i in range(t)]
    piv = vecs[0]
    vecs.sort(key= lambda x: dot(x[0], piv[0]), reverse=True)
    max_cos = dot(piv[0], vecs[1][0])
    a, b = vecs[0][1], vecs[1][1]
    for i in range(1, len(vecs)):
        cos = dot(vecs[i][0], vecs[i-1][0])
        if cos > max_cos:
            max_cos = cos
            a, b = vecs[i-1][1], vecs[i][1]
    print(a+1, b+1)

    




# Set the stack size
threading.stack_size(1 << 27)

# Create and start the main thread
main_thread = threading.Thread(target=main)
main_thread.start()

# Wait for the main thread to complete
main_thread.join()

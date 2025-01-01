import sys, threading
input = sys.stdin.readline
from collections import defaultdict, Counter
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

def gcd(t):
    a, b = t
    a, b = abs(a), abs(b)
    if a < b:
        a, b = b, a
    if b == 0:
        return a

    return gcd((b, a%b))

def sign(x):
    return abs(x[0]*x[1])//x[0]*x[1]
def main():
    n = int(input())
    a =  list(map(int, input().split()))
    b =  list(map(int, input().split()))
    f = Counter(map(lambda x: (sign(x)*abs(x[0])//gcd(x), abs(x[1])//gcd(x))  if x[0]*x[1] != 0 else (0, 0), zip(a, b))).items()
    c = list(f)
    d = len(list(filter(lambda x: x[0] == 0 and x[1] == 0, zip(a, b))))
    c.sort(key = lambda x: x[1])
    # d.sort(key = lambda x: x[1])
    if c[-1][0][0]:
        print(c[-1][1] + d)

    else:
        c.pop()
        if c:
            d+=c[-1][1]

        print(d)
    




# Set the stack size
threading.stack_size(1 << 27)

# Create and start the main thread
main_thread = threading.Thread(target=main)
main_thread.start()

# Wait for the main thread to complete
main_thread.join()

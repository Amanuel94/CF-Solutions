import sys, threading
input = sys.stdin.readline
from collections import defaultdict
input = sys.stdin.readline
MOD = 10**9 + 7
power = {0:1}
# returns the first number where key becomes true for a given delegate type key
def bs(low=1, high=1, key = lambda x: True):

    while low <= high:
        mid = (low + high)//2
        if key(mid):
            high = mid-1
        else:
            low = mid+1
    return low

def addLast(hash_val, last):
    return (hash_val*27+ ord(last) - 96)%MOD

def pollFirst(hash_val, first, n):
    return (hash_val - (ord(first) - 96)*power[n-1])%MOD

def conc(hash_val1, hash_val2, m):
    return (hash_val1*power[m] + hash_val2)%MOD


def main():
    s = input().strip()
    t = input().strip()


    for i in range(1, len(s)):
        power[i] = (power[i-1]*27)%MOD

    d_hash = 0
    s_hash = 0


    for i in range(len(t)):
        d_hash = addLast(d_hash, t[i])
        s_hash = addLast(s_hash, s[i])
    s_hash = addLast(s_hash, s[-1])

    left = 0     
    right = pollFirst(s_hash, s[0], len(s))
    ans = []
    for i in range(len(s)-1):
        if conc(left, right, len(s) - 1 - i) == d_hash:
            ans.append(i+1)
        left = addLast(left, s[i])
        right = pollFirst(right, s[i+1], len(s) - i - 1)
    if conc(left, right, 0) == d_hash:
            ans.append(len(s))
    print(len(ans))
    print(*ans)
    




# Set the stack size
threading.stack_size(1 << 27)

# Create and start the main thread
main_thread = threading.Thread(target=main)
main_thread.start()

# Wait for the main thread to complete
main_thread.join()

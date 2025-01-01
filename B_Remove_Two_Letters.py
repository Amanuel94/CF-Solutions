import sys, threading
input = sys.stdin.readline
from collections import defaultdict
input = sys.stdin.readline
MOD = 10**9+7
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
    t = int(input())
    for _ in range(t):
        n = int(input())
        s =  input().strip()
        hash_val = 0
        for i in range(1, n):
            power[i] = (power[i-1]*27)%MOD
        for c in s:
            hash_val = addLast(hash_val, c)

        seen = set()
        left = 0
        right = pollFirst(pollFirst(hash_val, s[0], n), s[1], n-1)
        # print(hash_val, conc(addLast(addLast(0, s[0]), s[1]), right, n-2))
        ans = 1
        seen.add(conc(left, right, n-2))
        for i in range(2, n):
            left = addLast(left, s[i-2])
            right = pollFirst(right, s[i], n - i)
            seen.add(conc(left, right, n-i-1))

        print(len(seen))


        


    




# Set the stack size
threading.stack_size(1 << 27)

# Create and start the main thread
main_thread = threading.Thread(target=main)
main_thread.start()

# Wait for the main thread to complete
main_thread.join()

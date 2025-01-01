from functools import cache
import sys, threading
input = sys.stdin.readline
input = sys.stdin.readline


def bit_length(n):
    count= 0
    while n:
        n>>=1
        count+=1
    return count

# @cache
def findI(i, s):
    if i in s:
        return s[i]
    else:
        return findI(i - pow(2, bit_length(i)-1), s)

def main():
    
    n, l, r =  list(map(int, input().split()))
    if n == 0:
        print(0)
    else:
        s = {}
        c = 0
        k = pow(2, bit_length(n)-1)
        while n:
            s[k] = n&1
            n>>=1
            k//=2
        # for s 
        # print(s)
        sum_ = 0
        for i in range(l, r+1):
            sum_+= findI(i, s)
        print(sum_)


# Set the stack size
threading.stack_size(10**6)

# Create and start the main thread
main_thread = threading.Thread(target=main)
main_thread.start()

# Wait for the main thread to complete
main_thread.join()

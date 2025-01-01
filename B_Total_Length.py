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
    n, s =  list(map(int, input().split()))
    a = list(map(int, input().split()))
    left= 0
    right = 0
    sum_ = 0
    ans = [0]*n
    while right < n:
        if sum_ + right <= s:
            sum_+=a[right]
            ans[left]+=right-left+1
            right+=1
        else:
            sum_-=a[left]
            left+=1
            ans[left]+=ans[left-1] - (right - left +1)
        print(left,right, sum_)
    print(ans)
    print(sum(ans))








# Set the stack size
threading.stack_size(1 << 27)

# Create and start the main thread
main_thread = threading.Thread(target=main)
main_thread.start()

# Wait for the main thread to complete
main_thread.join()

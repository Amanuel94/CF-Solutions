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
# 3 2 1 5 4 3 2 1 5 4
# 1 1 2 1 1 1 1 2 1 1

def find(numsi):
    m = len(numsi)
    nums = numsi*2
    i = 0
    count = 1
    while i < len(nums)-1:
        if nums[i] <= nums[i+1]:
            count+=1
        else:
            count =  1
        if count == m:
            return i+2-m, i+1
        i+=1
    return inf, -inf

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        nums =  list(map(int, input().split()))
        if nums == sorted(nums): 
            print(0)
            continue
        a, b = find(nums)
        c, d = find(nums[::-1])
        # print(a, b)
        # print(c, d)
        # print("4"*10)
        ans = min(min(a+2, 2*n - b - 1), min(c+1, 2*n-d))
        if ans == inf:
            print(-1)
            continue
        print(ans)
        

        
    




# Set the stack size
threading.stack_size(1 << 27)

# Create and start the main thread
main_thread = threading.Thread(target=main)
main_thread.start()

# Wait for the main thread to complete
main_thread.join()

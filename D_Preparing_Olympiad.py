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

    
    n, l, r, x = list(map(int, input().split()))
    nums =  list(map(int, input().split()))
    nums.sort()
    ans = 0


    def helper(mask):
        if mask == 0:
            return 0
        picks = [nums[i] for i in range(n) if (mask>>i )&1]
        # print(mask, picks)
        return abs(picks[0] - picks[-1]) 

    def backtrack(mask, i, sum_):
        nonlocal ans, n, l, r, x
        # print(mask)
        if i == n:
            return
        if sum_ > r:
            # print(sum_)
            return
        if l<=sum_ and helper(mask) >= x:
            # print(bin(mask))
            ans+=1
        for j in range(i, n):
            if (mask>>j)&1 == 0:
                backtrack((mask)|(1<<j), j, sum_+nums[j])
        
    backtrack(0, 0, 0)
    print(ans)
                
            
                




    




# Set the stack size
threading.stack_size(1 << 27)

# Create and start the main thread
main_thread = threading.Thread(target=main)
main_thread.start()

# Wait for the main thread to complete
main_thread.join()

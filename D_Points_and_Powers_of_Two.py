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
    n = int(input())
    nums =  list(map(int, input().split()))
    nums.sort()
    
    max_ans = 0
    max_p = -1
    for p in range(31):
        m = pow(2, p)
        expect = nums[0] + m
        count =  0
        for i in range(1, len(nums)):
            if nums[i] > expect:
                expect = nums[i] + m
                
            if nums[i] == expect:
                count+=1
                expect = nums[i] + m

        
        if count > max_ans:
            max_ans = count
            max_p = p
        if count == 2:
            break
    
    ans = []
    m = pow(2, max_p)
    expect = nums[0] + m
    for i in range(1, len(nums)):
            if nums[i] > expect:
                expect = nums[i] + m
                
            if nums[i] == expect:
                ans.append(nums[i])
                expect = nums[i] + m
    if not ans:
        print(1)
        print(nums[-1])
        return
    ans.append(ans[0]-m)
    print(len(ans))
    print(*ans)
    

    
    
            
        
    

    




# Set the stack size
threading.stack_size(1 << 27)

# Create and start the main thread
main_thread = threading.Thread(target=main)
main_thread.start()

# Wait for the main thread to complete
main_thread.join()

import sys, threading
input = sys.stdin.readline
from collections import defaultdict
input = sys.stdin.readline

def main():

    def cross(arr, low, mid, high):
        left = float('-inf')
        temp = 0
        
        for i in range(mid, low - 1, -1):
            temp += arr[i]
            if temp > left:
                left = temp
        
        right = float('-inf')
        temp = 0
        
        for i in range(mid + 1, high + 1):
            temp += arr[i]
            if temp > right:
                right = temp
        
        return left + right

    def max_sum(arr, low, high):
        if low == high:
            return arr[low]
        
        mid = (low + high) // 2
        
        left_max = max_sum(arr, low, mid)
        right_max = max_sum(arr, mid + 1, high)
        cross_max = cross(arr, low, mid, high)
        
        return max(left_max, right_max, cross_max)




    t = int(input())
    for _ in range(t):
        n = int(input())
        nums =  list(map(int, input().split()))

        max_pre_right = max_sum(nums, 1, len(nums)-1)
        max_pre_left = max_sum(nums, 0, len(nums)-2)
        sum_ = sum(nums)
        if max(max_pre_left, max_pre_right) >= sum_:    
            print("NO")
        else:
            print("YES")
        

    




# Set the stack size
threading.stack_size(1 << 27)

# Create and start the main thread
main_thread = threading.Thread(target=main)
main_thread.start()

# Wait for the main thread to complete
main_thread.join()

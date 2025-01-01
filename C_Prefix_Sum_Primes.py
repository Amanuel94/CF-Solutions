import sys, threading
input = sys.stdin.readline
from collections import defaultdict
input = sys.stdin.readline

def main():
    n = int(input())
    nums =  list(map(int, input().split()))

    
    
    n_ones = n_twos = 0
    for num in nums:
        n_ones += int(num ==  1)
        n_twos += int(num == 2)
    
    if n_ones*n_twos == 0:
        print(*nums)
        exit()

    ans = []
    if 0 < n_ones <= 2:
        ans.append(2)
        ans.append(1)
        ans = ans + [2]*(n_twos-1)
        ans = ans + [1]*(n_ones-1)
        print(*ans)
    elif n_ones%2:
        nums.sort()
        print(*nums)
    else:
        ans = [1]*(n_ones-1) + [2]*(n_twos) + [1]
        print(*ans)



# Set the stack size
threading.stack_size(1 << 27)

# Create and start the main thread
main_thread = threading.Thread(target=main)
main_thread.start()

# Wait for the main thread to complete
main_thread.join()

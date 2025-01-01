import sys, threading
input = sys.stdin.readline
from collections import defaultdict
input = sys.stdin.readline

def main():
    n, k ,p =  list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.sort()
    b.sort()

    # dp[i][j] = person i takes key j
    dp = [[float('inf')]*(n+1) for i in range(k+1)]
    # print(dp)
    # exit()
    dp[0][0] = 0 
    # print(dp)
    for i in range(1, k+1):
        
        for j in range(n+1):
            dp[i][j] = min(dp[i][j], dp[i-1][j])
            if j < n:
                dp[i][j+1] = min(
                    dp[i][j+1],
                max(
                    abs(a[j] - b[i-1]) + abs(b[i-1]-p),
                    dp[i-1][j]
                ))
        # print(dp)
    print(dp[k][n])
    




# Set the stack size
threading.stack_size(1 << 27)

# Create and start the main thread
main_thread = threading.Thread(target=main)
main_thread.start()

# Wait for the main thread to complete
main_thread.join()

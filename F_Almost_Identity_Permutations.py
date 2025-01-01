import sys, threading
input = sys.stdin.readline
from collections import defaultdict
input = sys.stdin.readline


"""
abcd.. n
f(n, k)= f(n-1, k) + (n-1)*f(n-1, k-2)
123 0
132 2
213 2
231 3
312 3
321 2
abcde

0 0 0
1 0 0
1 0 2
1 0 5

f(3,3) = f(2,3) = f(1,3)+ 
[[0, 0, 0, 0],
 [1, 0, 0, 0],
 [1, 0, 1, 0]
 [1, 0, 3, 0],
 [1, 0, 6, 0],
 [1, 0, 10, 0]]

"""

def main():
    n,k =  list(map(int, input().split()))

    dp = [[0]*(k+1) for i in range(n+1)]
    for s in range(1, n+1):
        dp[s][0] = 1
    for i in range(1, n+1):
        for j in range(2, k+1):
                if i >= j:
                    dp[i][j] += dp[i-1][j] + (i-1)*dp[i-1][j-2]
    print(dp)
    print(sum(dp[n]))
    




# Set the stack size
threading.stack_size(1 << 27)

# Create and start the main thread
main_thread = threading.Thread(target=main)
main_thread.start()

# Wait for the main thread to complete
main_thread.join()

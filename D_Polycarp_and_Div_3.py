import sys, threading
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def main():
    
    
    pre = [0]
    for num in list(map(int, list(input().strip()))):
        pre.append(pre[-1]+num)
    # print(pre)

    memo = {}
    ans = float('inf')
    def dp(ptr):
        if ptr == 1:
            memo[ptr] = int(pre[ptr]%3 == 0)
        if ptr in memo:
            return memo[ptr]
        elif ptr == 0:
            memo[ptr] = 0
        
        else:
            i = ptr-1
            while i >= 0:
                cur =int((pre[ptr]-pre[i])%3 == 0)
                if ptr in memo:
                    if i in memo:
                        memo[ptr] = max(cur + memo[i], memo[ptr])
                    else:
                        memo[ptr] = max(cur + dp(i), memo[ptr])
                    # break
                else:
                    if i in memo:
                        memo[ptr] = cur + memo[i]
                    else:
                        memo[ptr] = cur + dp(i)
                    # break
                if cur:
                    break
                i-=1
        return memo[ptr]
    print(dp(len(pre)-1))

    # Set the stack size
threading.stack_size(1 << 27)

    # Create and start the main thread
main_thread = threading.Thread(target=main)
main_thread.start()

    # Wait for the main thread to complete
main_thread.join()
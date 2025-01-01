import sys, threading
input = sys.stdin.readline
from collections import defaultdict
input = sys.stdin.readline

def main():
    t = int(input())
    # n = 0
    ns = []
    for _ in range(t):
        ns.append(int(input())) 
    max_ = max(ns) 
    
    dp = [float('inf')]*max(max_+7, 8)
    dp2 = [float('inf')]*max(max_+7, 8)
    # cost = [(6,0),(2,1),(5,2),(5,3),(4,4),(5,5),(6,6),(3,7),(7,8),(6,9)]
    # cost.sort(key = lambda x: (-x[1], x[0]))
    dp[2] = 1
    dp[3] = 7
    dp[4] = 4
    dp[5] = 2
    dp[6] = 0
    dp[7] = 8
    for i in range(2, max_):
        for k in range(2, 7):
            dp[i+k] = min(dp[k]*pow(10, len(str(dp[i])))+dp[i], dp[i+k])
            dp2[i+k] = min(dp[k]*pow(10, len(str(dp[i])))+dp[i], dp[i+k]) 
    # print(dp)
    for n in ns:
        r = n
        ans = 0
        if n%2:
            i = 0
            while n-3:
                ans+=pow(10, i)
                n-=2
                i+=1
            
            ans+= 7*pow(10, i) 
        else:
            i = 0
            while n:
                ans+=pow(10, i)
                n-=2
                i+=1
        if dp[r] == 0 and r > 6:
            r = n
            ans = 0
            if n%2:
                i = 0
                while n-3:
                    ans+=pow(10, i)
                    n-=2
                    i+=1
                
                ans+= 7*pow(10, i) 
            else:
                i = 0
                while n:
                    ans+=pow(10, i)
                    n-=2
                    i+=1

        print(dp[r], ans)


            


    




# Set the stack size
threading.stack_size(1 << 27)

# Create and start the main thread
main_thread = threading.Thread(target=main)
main_thread.start()

# Wait for the main thread to complete
main_thread.join()

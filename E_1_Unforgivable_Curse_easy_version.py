import sys, threading
sys.setrecursionlimit(10*3)
input = sys.stdin.readline
from collections import Counter
t_ = int(input())
def main():
    global t_

    def check(s, t):
            if len(s) != len(t):
                return False
            for k in s:
                if k not in t or s[k]!= t[k]:
                    return False
            return True

    def f(s,t, n):
            
            if s == t:
                return True
            

            if n >= 6:
                return check(Counter(s), Counter(t))
            elif n == 5:
                return s[2] == t[2]
            elif n==4:
                # print(s, t)
                return s == t
            elif n <= 3:
                return t == s
        
    for _ in range(t_):
        n, m = list(map(int, input().split()))
        s =  input().strip()
        t = input().strip()
        print("YES") if f(s,t,n) else print("NO")

    # Set the stack size
threading.stack_size(1 << 27)

    # Create and start the main thread
main_thread = threading.Thread(target=main)
main_thread.start()

    # Wait for the main thread to complete
main_thread.join()


    


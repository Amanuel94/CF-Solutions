import sys, threading
input = sys.stdin.readline
from collections import defaultdict
inf = float('inf')
# returns the first number where key becomes true for a given delegate type key NNSN RH  RHRR 
def bs(low=1, high=1, key = lambda x: True):

    while low <= high:
        mid = (low + high)//2
        if key(mid):
            high = mid-1
        else:
            low = mid+1
    return low


def main():
    t = int(input())
    for _ in range(t):
        n =  int(input())
        s = input().strip()
        N = E = 0
        ans = []
        for c in s:
            if c == 'N':
                N += 1
            if c == 'S':
                N -= 1
            if c == 'E':
                E += 1
            if c == 'W':
                E -= 1
        if N%2 != 0 or E%2 != 0:
            print("NO")
            continue


        n, e = N, E
        pick = ['R', 'H']
        for c in s:
            if c == 'N':
                N -= 1
                if n > 0: ans.append(pick[N%2])
                else : ans.append("R")
            if c == 'S':
                
                if n > 0:
                    ans.append("R")
                    N += 1
                else: 
                    ans.append(pick[N%2])
                    N-=1
                
            if c == 'E':
                E -= 1
                if e > 0: ans.append(pick[E%2])
                else : ans.append("R")
            if c == 'W':
                # E += 1
                if e > 0: ans.append("R")
                else : ans.append(pick[E%2])
        print("".join(ans))

        




# Set the stack size
threading.stack_size(1 << 27)

# Create and start the main thread
main_thread = threading.Thread(target=main)
main_thread.start()

# Wait for the main thread to complete
main_thread.join()

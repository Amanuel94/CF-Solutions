from functools import cache
import sys, threading
input = sys.stdin.readline
from collections import defaultdict, deque
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


pows = set([str(1<<i) for i in range(32)])
# print(pows)
# @cache
@cache
def solve(n, ):
    # q = deque([str(n)])
    # ans = 0
    # vis = set([str(n)])
    # while q:
    #     l = len(q)
    #     for _ in range(l):
    #         x = q.popleft()
    #         if x in pows:
    #             return ans
            
    #         op1 = erase(x)
    #         op2 = appen(x)
            

    #         for nbr in op1:
    #             if nbr not in vis:
    #                 q.append(nbr)
    #                 vis.add(nbr)
            
    #         for nbr in op2:
    #             if nbr not in vis:
    #                 q.append(nbr)
    #                 vis.add(nbr)
    #     ans +=1
    # return ans


                
            
            

# def erase(n):
    
#     ans = []
#     # if len(n) > 0 and n[0] == '0':
#     #     return []
#     for i in range(len(n)):
#         ans.append(n[:i] + n[i+1:])
#     return ans

# def appen(n):
#     ans = []
#     if len(n) > 9:
#         return []
#     if len(n) > 8:
#         return ["1" + n]
    
#     if len(n) > 0 and n[0] == '0':
#         return []
    
#     for i in range(10):
#         ans.append(n + str(i))
        
#     return ans

            


def main():
    t = int(input())
    for _ in range(t):
        n =  int(input())
        # print(erase(str(n)))
        print(solve(n))
        

    




# Set the stack size
threading.stack_size(1 << 27)

# Create and start the main thread
main_thread = threading.Thread(target=main)
main_thread.start()

# Wait for the main thread to complete
main_thread.join()

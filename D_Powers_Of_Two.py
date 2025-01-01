import sys, threading
input = sys.stdin.readline
from collections import defaultdict, deque
input = sys.stdin.readline

def main():
    def count_set_bits(n):
        count = 0
        len_ = 0
        while n:
            count += n & 1
            len_+=1
            n >>= 1
        return count,len_ 

    n, k =  list(map(int, input().split()))
    set_, len_ = count_set_bits(n)
    if(set_<=k<=n):
        print("YES")
        q = deque([])
        
        i = 0
        while i < len_:
            if(n) & 1:
                q.append(1<<i)
            n>>=1
            i+=1
        while len(q) < k:
            x = q.pop()
            if x != 1:
                q.appendleft(x//2)
                q.appendleft(x//2)
            else:
                q.appendleft(x)
            
                
        print(*q)

    else:
        print("NO")
    



main()

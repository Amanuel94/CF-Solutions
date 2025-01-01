import sys, threading
input = sys.stdin.readline
from collections import defaultdict, deque
input = sys.stdin.readline

def main():
    n, m =  list(map(int, input().split()))
    s = input().strip()
    # s = list(map(lambda x:ord(x)-97, inpnut().strip()))
    G = defaultdict(list)
    
    inc = defaultdict(int)
    for _ in range(m):
        x, y = list(map(int, input().split()))
        G[y].append(x)
        inc[x-1]+=1
    q = deque([i+1 for i in range(n) if inc[i] == 0])
    map_ = [[0]*26 for i in range(n)]
    count = len(q)
    while q:
        a = q.popleft()
        map_[a-1][ord(s[a-1])-97]+=1
        for nbr in G[a]:
            inc[nbr-1]-=1
            for i in range(26):
                map_[nbr-1][i] = max(map_[a-1][i], map_[nbr-1][i])
            if inc[nbr-1] == 0:
                q.append(nbr)
                count+=1
    if count!= n:
        print(-1)
    else:
        print(max([max(f) for f in map_]))
main()
                

            
        

        
    

            


    





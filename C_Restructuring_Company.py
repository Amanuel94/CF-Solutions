from collections import defaultdict
class UnionFind:
    def __init__(self, size) -> None:

        self.dict =  defaultdict(int)
        self.size = defaultdict(int)
        for _ in range(size):
            self.dict[_+1] = _+1
            self.size[_] = 1
    
    def representative(self, x):

        parent = self.dict[x]
        while self.dict[parent] != parent:
            parent = self.dict[parent]
        
        while x != self.dict[x]:
            self.dict[x] = parent
            x = self.dict[x]
        return parent
    
    def union(self, x, y):
        rep_x, rep_y =  self.representative(x), self.representative(y)
        if self.size[rep_x] < self.size[rep_y]:
            self.size[rep_y] =  max(self.size[rep_x]+1, self.size[rep_y])
            self.dict[rep_x] = rep_y
        else:
            rep_x, rep_y = rep_y, rep_x
            self.size[rep_y] =  max(self.size[rep_x]+1, self.size[rep_y])
            self.dict[rep_x] = rep_y
    def connected(self, x, y):
        return self.representative(x) == self.representative(y)
import sys
input = sys.stdin.readline
from collections import defaultdict, deque
# ran = defaultdict(int)
n, q  = list(map(int, input().split()))
uf = UnionFind(n)
ran = {i+1:i+1 for i in range(n)}
for _ in range(q):
    type, x, y = list(map(int, input().split()))
    if type == 1:
        uf.union(x, y)
    elif type == 2:
        i = x
        while i < y:
            uf.union(i, i+1)
            if i+1 != ran[i+1]:
                i = ran[i+1]-1
                if i >= y:
                    break
                # uf.union(i, i+1)
            i+=1
            ran[i-1] = max(ran[i-1], y) 
         
    else:
        if uf.connected(x, y):
            print('YES')
        else:
            print('NO')


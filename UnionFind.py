from collections import defaultdict
class UnionFind:
    def __init__(self, size) -> None:

        self.dict =  defaultdict(int)
        self.size = defaultdict(int)
        for _ in range(size):
            self.dict[_] = _
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

uf = UnionFind(10)
# 1-2-5-6-7 3-8-9 4
uf.union(1, 2)
uf.union(2, 5)
uf.union(5, 6)
uf.union(6, 7)
uf.union(3, 8)
uf.union(8, 9)
print(uf.connected(1, 5))  # true
print(uf.connected(5, 7))  # true
print(uf.connected(4, 9))  # false
# 1-2-5-6-7 3-8-9-4
uf.union(9, 4)
print(uf.connected(4, 9))  # true



class Trie:

    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, num):
        ptr = self.root
        bit = bin(num)[2:].zfill(31)
        for c in bit:
            i = int(c)
            if ptr.children[i] is None:
                ptr.children[i] = TrieNode()
            ptr = ptr.children[i]
        ptr.val = num

    def findCompliment(self, num):
        ptr = self.root
        bit = bin(num)[2:].zfill(31)

        for c in bit:
            i = int(c)
            if ptr.children[1-i] is not None:
                ptr = ptr.children[1-i]
            else:
                ptr = ptr.children[i]
        return ptr.val



class TrieNode:
    def __init__(self):
        self.children = [None]*2
        self.val = -1

class Solution:
    def findMaximumXOR(self, nums) -> int:

        trie = Trie()
        for num in nums:
            trie.insert(num)
        max_xor = 0
        for num in nums:
            max_xor = max(max_xor, num ^ trie.findCompliment(num))
        return max_xor

t = int(input())
for i in range(t):
    n = int(input())
    print(Solution().findMaximumXOR(list(map(int, input().split()))))
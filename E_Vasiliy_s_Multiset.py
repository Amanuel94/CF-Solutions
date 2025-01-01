class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.max_bit_len = 32
    
    def insert(self, num):
        ptr = self.root        
        for j in range(self.max_bit_len, -1, -1):
            ptr.count+=1
            i = (num>>j)&1
            if i == 0:
                if ptr.zero is None:
                    ptr.zero= TrieNode()
                ptr = ptr.zero
            else:
                if ptr.one is None:
                    ptr.one = TrieNode()
                ptr = ptr.one

        
           
        ptr.val = num
        ptr.count+=1

    def remove(self, num):
        ptr = self.root        
        for j in range(self.max_bit_len, -1, -1):
            ptr.count-=1
            i = (num>>j)&1
            if i == 0:
                ptr = ptr.zero
            else:
                ptr = ptr.one
        ptr.count-=1

    def findXOR(self, num):

        ptr = self.root        
        for j in range(self.max_bit_len, -1, -1):
            i = (num>>j)&1
            if i == 0:
                if ptr.one and ptr.one.count:
                    ptr = ptr.one
                else:
                    ptr = ptr.zero
            else:
                if ptr.zero and ptr.zero.count:
                    ptr = ptr.zero
                else:
                    ptr = ptr.one
        return ptr.val


class TrieNode:
    def __init__(self):
        self.zero = None
        self.one = None
        self.count = 0
        self.val = -1

import sys, threading
input = sys.stdin.readline
from collections import defaultdict


# returns the first number where key becomes true for a given delegate type key
def bs(low=1, high=1, key = lambda x: True):

    while low <= high:
        mid = (low + high)//2
        if key(mid):
            high = mid-1
        else:
            low = mid+1
    return low


def main():
    q = int(input())
    trie = Trie()
    trie.insert(0)
    for _ in range(q):


        op, num = input().split()
        num = int(num)

        if op == "+":
            trie.insert(num)
        if op == "-":
            trie.remove(num)
        if op == "?":
            print(num ^ trie.findXOR(num))

    



main()

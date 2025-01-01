
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word: str) -> None:
        ptr = self.root
        
        for i, c in enumerate(word):
            ptr.count+=1
            c = ord(c)-97
            if ptr.children[c] is  None:
                ptr.children[c] = TrieNode()
            
            ptr = ptr.children[c]
        ptr.count+=1
        ptr.is_end = True

    def search(self, word: str)-> None:

        prefix, is_end = self.searchPrefix(word)
        return prefix == word and is_end

    def searchPrefix(self, word:str) -> None:

        ptr =  self.root
        i = 0
        prefix = ""
        while ptr and i < len(word):
            c = ord(word[i])-97
            ptr = ptr.children[c]
            if ptr:
                prefix+=word[i]
            i+=1

        if ptr:
            return prefix, ptr.is_end
        return prefix, False

    def startsWith(self, word:str) -> None:

        prefix, is_end = self.searchPrefix(word)
        return prefix == word
    
    def findMaxPre(self, word:str):
        ptr = self.root
        i = 0
        count = 0

        while i < len(word):
            ptr = ptr.children[ord(word[i]) - ord('a')]
            i+=1
            if ptr and ptr.count > 1:
                count+=1    

        return count



class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [ None for _ in range(26) ]
        self.count = 0

import sys, threading
input = sys.stdin.readline
from collections import defaultdict
input = sys.stdin.readline

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
    t = int(input())
    trie = Trie()
    words = []
    for _ in range(t):
        words.append(input().strip())
        trie.insert(words[-1])

    for s in words:
        print(trie.findMaxPre(s))
   

    
    
    




main()
import sys, threading
input = sys.stdin.readline
from collections import defaultdict
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

class TrieNode:
    def __init__(self, val = 0):
        self.val = val
        self.children = defaultdict(TrieNode)
        self.isEnd = 0
    
    def insert(self, word):
        node = self
        for ch in word:
            node = node.children[ch]
        node.isEnd = 1


def Trie:



def main():
    t = int(input())
    nums =  list(map(int, input().split()))
    




# Set the stack size
threading.stack_size(1 << 27)

# Create and start the main thread
main_thread = threading.Thread(target=main)
main_thread.start()

# Wait for the main thread to complete
main_thread.join()

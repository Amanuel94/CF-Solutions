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

    def __init__(self):
        self.children = [None, None]
        self.is_end = -1
    
class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.ind = 0
      

    
    def insert(self, num, n, i):
        ptr = self.root
        for j in range(n, -1, -1):
            cur = (num >> j) & 1
            if ptr.children[cur] is None:
                ptr.children[cur] = TrieNode()
            ptr = ptr.children[cur]    
        ptr.is_end = i 



def main():
    t = int(input())
    for _ in range(t):
        n, k =  list(map(int, input().split()))
        a = list(map(int, input().split()))

    




# Set the stack size
threading.stack_size(1 << 27)

# Create and start the main thread
main_thread = threading.Thread(target=main)
main_thread.start()

# Wait for the main thread to complete
main_thread.join()

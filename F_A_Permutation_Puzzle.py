import sys, threading
input = sys.stdin.readline
from collections import defaultdict
from math import lcm
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


def findStr(i, p, s, seen):
    start = p[i-1]
    ans = s[i-1]
    seen.add(i)
    while start !=  i:
        seen.add(start)
        ans += s[start-1]
        start = p[start-1]
    seen.add(start)
    return  ans

def matchStr(s):
    t = s+s
    r = len(s)
    i = 1
    while i < len(s) and t[i:len(s)+i] != s:
        i+=1
    
    return i


    
def gcd(a, b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a

    return gcd(b, a%b)

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = input().strip()
        p =  list(map(int, input().split()))
        seen = set()
        # print(findStr(1, p, s, seen))
        # print(matchStr("aba"))
        ans = 0
        g = None
        l = None
        li = []
        prod = 1
        for i in range(len(p)):
            if i+1 not in seen:
                pat = findStr(i+1, p, s, seen)
                ans = matchStr(pat)
                prod *= ans

                if l is None:
                    g = ans
                else:
                    g = gcd(g, ans)
                    
                    l = prod//g
                li.append(ans)
        print(lcm(*li))

        
        




# Set the stack size
threading.stack_size(1 << 27)

# Create and start the main thread
main_thread = threading.Thread(target=main)
main_thread.start()

# Wait for the main thread to complete
main_thread.join()

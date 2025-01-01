import sys
input = sys.stdin.readline
from collections import defaultdict, deque

p = {chr(i) :chr(i) for i in range(97, 97+26)}
inc = [1]*26
def getP(x):
    parent = p[x]
    while p[parent] != parent:
        parent = p[parent]
        
    while x != p[x]:
        p[x] = parent
        x = p[x]
    return parent

n  =  int(input())
s1 = input()
s2 = input()
for i in range(n):
    p[getP(s1[i])] = getP(s2[i])



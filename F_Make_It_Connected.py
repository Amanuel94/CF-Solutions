import sys
input = sys.stdin.readline
from collections import defaultdict, deque
from heapq import heapify, heappush, heappop

n,  m = list(map(int, input().split()))
a_ = list(map(int, input().split()))
offers = []
for _ in range(m):

    offers.append(list(map(int, input().split())))
# print(offers)
a = [(ai, i+1) for i, ai in enumerate(a_)]
a.sort()
# ans = 0
a1, cent = a[0]
# i = 1
# ec = defaultdict(list)
# while i < len(a):
#     ai, leaf_i= a[i]
#     ans+=(ai+a1)
#     i+=1
#     heappush(ec[leaf_i], -(ai+a1))
#     heappush(ec[cent], -(ai+a1))
# # ans+=(n-1)*a1
# print(dict(ec))
# for offer in offers:
#     x, y, w = offer
#     if -ec[x][0] <= -ec[y][0]:
#         if w < max(-ec[y][0], -ec[x][0]):
#             ans+=heappop(ec[y])
#             ans+=w
#             heappush(ec[x], -w)
#             heappush(ec[y], -w)
#     else:
#         if w < max(-ec[y][0], -ec[x][0]):
#             ans+=heappop(ec[x])
#             ans+=w
#             heappush(ec[x], -w)
#             heappush(ec[y], -w)
        

# print(ans)
# print(a)
offers = sorted(offers, key=lambda x: x[2])
# print(offers)
ans = 0
p = {i:i for i in range(1,n+1)}
def getP(i):
    if i == p[i]:
        return i
    p[i] = getP(p[i])
    return p[i]
for offer in offers:
    x, y, w = offer
    if x > y:
        x, y = y, x
    if getP(x) != getP(y):
        if w-a1 < max(a_[getP(x)-1], a_[getP(y)-1]):
            ans+=w
            if a_[getP(x)-1] <= a_[getP(y)-1]:
                p[getP(y)] = getP(x)
            else:
                p[getP(x)] = getP(y)
immed = set()
# print(p)
for i in range(1, n+1):
    immed.add(getP(i))
for i in immed:
    if i != cent:
        ans+=(a_[i-1] + a1)
print(ans)





N, D = list(map(int, input().split()))
P = sorted(list(map(int, input().split())), reverse= True)
l = 0
r = len(P)-1

cur = P[l]
ans = 0
while l < r:
    if cur <= D:
        cur+= P[l]
        r-=1
    else:
        ans+=1
        l+=1
        cur = P[l]
if cur > D:
    ans+=1

print(ans)

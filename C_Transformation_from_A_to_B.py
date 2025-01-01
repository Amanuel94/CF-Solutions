import sys
from collections import defaultdict
input = sys.stdin.readline

a, b  = list(map(int, input().split()))
ans = [b]
def backtrack(a, b):
    if b == a:
        # ans.append(b)
        return True
    elif b < a:
        return False
    if b%2 == 0:
        ans.append(b//2)
        if backtrack(a, b//2):
            return True
        ans.pop()
    if(b-1)%10 == 0:
        ans.append((b-1)//10)
        if backtrack(a, ((b-1)//10)):
            return True
        ans.pop()
    
    return False
# ans.revers
if backtrack(a, b):
    print("YES")
    ans.reverse()
    print(len(ans))
    print(*ans)
else:
    print("NO")


        
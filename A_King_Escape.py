import math
import sys
input = sys.stdin.readline


#check if in check
def inCheck(x, y, qx, qy):
    if x == qx or y == qy or (x+y == qx+qy) or x-y == qx - qy:
        return True
    else:
        return False

#check if in same quad
def inQuad(x, y, cx, cy, qx, qy):
    if x < qx and cx > qx or  x > qx and cx < qx:
        return False
    if  y < qy and cy > qy or  y > qy and cy < qy:
        return False
    return True

n = int(input())
qx, qy =  list(map(int, input().split()))
x, y = list(map(int, input().split()))
cx, cy = list(map(int, input().split()))

if not inCheck(x, y, qx, qy) and inQuad(x, y, cx, cy, qx, qy) and not inCheck(cx, cy, qx, qy) :
    print("YES")
else:
    print('NO')




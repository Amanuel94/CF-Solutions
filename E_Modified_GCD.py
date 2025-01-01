a, b = list(map(int, input().split()))

def gcd(a,b):

    if b == 0:
        return a
    return gcd(b, a%b)

n = int(input())
h = gcd(a, b)
# print(g)
for _ in range(n):
    low, high = list(map(int, input().split()))
    # ans=  -1
    # for f in range(low, high+1):
    #     if g%f == 0:
    #         ans = f
    g = h
    # if low <= g <= high:
    #     print(g)
    
    d = 2
    f= 0
    while d*d <= g:
        while g%d == 0:
            if low <= g <= high:
                print(g)
                f = 1
                break
            g//=d
        d+=1
    if not f and low <= g <= high:
        print(g)
    elif not f:
        print(-1)

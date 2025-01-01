t =  int(input())

for _ in range(t):
    n =  int(input())
    a =  list(map(int, input().split()))

    a.sort()

    l = 0
    r = len(a)

    red = a[l]
    blue = 0

    while l < r:
        if l < len(a)-r and blue > red:
            break
        elif l < len(a)-r and blue <= red:
            r-=1
            blue+=a[r]
        else:
            l+=1
            red+=a[l]
    if l < r:
        print('Yes')
    else:
        print('No')
        
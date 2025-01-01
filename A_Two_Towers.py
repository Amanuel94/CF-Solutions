t =  int(input())

for _ in range(t):
    n,m = list(map(int, input().split()))
    B1 = input()
    B2 = input()

    B = B1+B2[::-1]
    prev = None
    count = 0
    for c in B:
        if prev == c:
            count+=1
        prev = c
    
    if count > 1:
        print('NO')
    else:
        print('YES')

t = int(input())

for _ in range(t):
    n, k =  list(map(int, input().split()))
    pre = [0]*51
    for __ in range(n):
        l, r = list(map(int, input().split()))

        if l <= k <= r:
            pre[l-1]+=1
            pre[r]-=1
    i = 1
    while i < len(pre):
        pre[i]+=pre[i-1]
        i+=1

    # print(pre)

    if k == 1:
        if pre[k-1] > pre[k]:
            print('YES')
        else:
            print('NO')
    elif k-1 < 50:
        if  pre[k-2] < pre[k-1]  and pre[k-1] > pre[k]:
            print('YES')
        else:
            print('NO')
    else:
        if pre[k-2] < pre[k-1]:
            print('YES')
        else:
            print('NO')
         
            

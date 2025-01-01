t =  int(input())

for _ in range(t):
    n =  int(input())

    likes = list(map(int, input().split()))
    pos = neg = 0
    for like in likes:
        if like > 0:
            pos+=1
        else:
            neg+=1

    for i in range(pos):
        print(i+1, end=" ")
    for j in range(neg):
        print(pos - j - 1, end = ' ')

    print()

    while neg:
        print('1 0', end=" ")
        pos-=1
        neg-=1

    for i in range(pos):
        print(i+1, end=" ")

    print()
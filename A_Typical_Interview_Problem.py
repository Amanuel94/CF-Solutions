t =  int(input())

for _ in range(t):

    s = "FBFFBFFB"
    s*=3

    n =  int(input())
    seq  =  input()

    if seq in s:
        print('YES')
    else:
        print('NO')
 
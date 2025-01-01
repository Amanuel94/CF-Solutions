t =  int(input())

for _ in range(t):

    a =  input()
    b = input()

    if a[0] == b[0]:
        print('YES')
        print(a[0]+'*')

    elif a[-1] == b[-1]:
        print('YES')
        print('*' + a[-1])

    else:
        flag = False
        i = 0
        while i < len(a)-1:

            if a[i]+a[i+1] in b:

                print('YES')
                print('*' + a[i]+a[i+1]+'*')
                flag = True
                break

            i+=1
        if not flag:
            print('NO') 
            
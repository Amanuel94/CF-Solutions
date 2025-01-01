t  = int(input())
stack = []
x = 0
N = 2**32 - 1
flag = 0
for _ in range(t):

    f = input().split()
    
    if f[0] ==  'add':
        cur = 1
        for op in stack:
            if float(cur) * float(op) <= N:
                cur*=op
            else:
                print('OVERFLOW!!!')
                flag = 1
                break
            if float(x) + float(cur) > N:
                print('OVERFLOW!!!')
                flag = 1
                break
            else:
                x+=cur
            

    elif f[0] == 'for':
        stack.append(int(f[-1]))
    elif f[0] == 'end':
        stack.pop()
if not flag:
    print(x)




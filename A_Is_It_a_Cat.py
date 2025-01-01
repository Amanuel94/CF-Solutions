t = int(input())
next = {
    'm':['m', 'e'],
    'e':['e', 'o'],
    'o':['o', 'w'],
    'w':['w']}

for _ in range(t):

    n =  int(input())
    sound = input()

    i = 0
    while i < n -1:
        if sound[i].lower() not in next or sound[i+1].lower() not in next[sound[i].lower()]:
            break
        i+=1

    if n >=4 and i == n-1 and sound[i].lower() == 'w' and sound[0].lower() == 'm':
        print('YES')
    else:
        print('NO')


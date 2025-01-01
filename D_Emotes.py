n, m , k =  list(map(int, input().split()))


emotes =  sorted(list(map(int, input().split())))

y = m // (k+1)
x = m%(k+1) + k*y

print(emotes[-1]*x + y*emotes[-2])


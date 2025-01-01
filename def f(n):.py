def f(n):
    c = 0
    while n >= 0:
        n -= 2
        c += n-2
    return c

for _ in range(100):
    print(_, f(_))

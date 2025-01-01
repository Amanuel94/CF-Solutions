l, r = list(map(int, input().split()))


def func(l, r):
    if l.bit_length() < r.bit_length():
        return 2**(r.bit_length())-1
    elif l == r:
        return 0
    else:
        l-= 1<<(l.bit_length()-1)
        r-= 1<<(r.bit_length()-1)
        return func(l, r)
    
print(func(l, r))
        


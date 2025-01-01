n  = int(input())
def factors(n):
    fact = [1]
    d = 2
    while d*d <= n:
        div = False
        while n%d == 0:
            div = True
            n//=d
        if div:
            fact.append(d)
        d+=1
    if n!= 1:
        fact.append(n)
    return fact

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

fact =  factors(n)
# if len(factors) == 1:
#     print(*[1, n])
# else:
#     fact = factors(n)
#     l = 0
#     r = len(fact-1)
#     ans = []
#     while l < r:

#         if l*r/gcd(l, r) == n:
#             ans = [l,r]
#         elif 

# fact2 = fact[:]
# print(fact)
if len(fact)==2:
    print(*[1, n])
else:
        pre = 1
        post = fact[-1]

        l = 0
        r=  len(fact)-1
        while l < r:
            
            if pre*fact[l] > post:
                post*=fact[r]
                r-=1
            else:
                pre*=fact[l]
                l+=1 

        print(*[pre, post])



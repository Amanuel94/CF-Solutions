t =  int(input())

def attack(secs, k):
    ans = 0
    i = 0
    while i < len(secs)-1:
        ans+= min(secs[i+1]-secs[i], k)
        i+=1
    ans+=k
    return ans


for _ in range(t):
    n, h =  list(map(int, input().split()))
    secs = list(map(int, input().split()))

    l =  0
    r =  h

    store = 0

    while l <= r:
        m = (l+r)//2

        if attack(secs, m) < h:
            store = l
            l = m +1
        else:
            # store = r
            r =  m-1

    # if attack(secs, m) >= h:
    print(l)

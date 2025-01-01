
n = int(input())
m = int(input())
r = m
a = []
for _ in range(n):
    a.append(int(input()))
max_ = max(a)
for ai in a:
    if m == 0:
        break
    if max_!=ai:
        m-=min(max_-ai, m)
t = 1-int(m%n==0)
print(max_+(m//n + t), max_+r)




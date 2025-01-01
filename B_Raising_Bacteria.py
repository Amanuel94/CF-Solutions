# import bit
n = bin(int(input()))[2:]

ans = 0
for c in n:
    ans+= int(c == '1')

print(ans)
import math
t = int(input())
N =  10**9 + 7
for _ in range(t):
    n, k =  list(map(int, input().split()))

    bin_k = bin(k)[2:][::-1]
    ans = 0
    for i, bit in enumerate(bin_k):

        if bit == '1':
            ans+= pow(n, i, N )

    print(ans%N)



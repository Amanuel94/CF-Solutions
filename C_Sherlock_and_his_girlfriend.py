def prime_sieve(n):
    prm = [1]*n
    ans = 1
    for i in range(2, n+2):
      
      if prm[i-2] == 1:
        j = 2*i
        col = 2

        while j <= n+1:
            if prm[j-2] == 1:
                prm[j-2] = col
                ans = max(ans, col)
                col+=1
               
            j+=i
        

    return ans, prm

import sys
input =  sys.stdin.readline
n = int(input())
ans, prm = prime_sieve(n)
print(ans)
print(*prm)



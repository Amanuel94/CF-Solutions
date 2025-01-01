import sys, threading
input = sys.stdin.readline
from collections import defaultdict
inf = float('inf')
# returns the first number where key becomes true for a given delegate type key
def bs(low=1, high=1, key = lambda x: True):

    while low <= high:
        mid = (low + high)//2
        if key(mid):
            high = mid-1
        else:
            low = mid+1
    return low

def factorization(n, k):
    factorization = {}
    i = 2
    while i*i <= n:

        while n%i == 0:
            if i not in factorization:
                factorization[i] = 0
            factorization[i] += 1
            factorization[i]%=k
            n//=i
        
        i+=1
    if n > 1:
        if n not in factorization:
            factorization[n] = 0
        factorization[n] += 1
        factorization[n]%=k
    
    return factorization



def main():
    n, k =  list(map(int, input().split()))
    nums =  list(map(int, input().split()))
    count = {}

    ans = 0

    for num in nums:

        equiv = 1
        comp = 1
        D = factorization(num, k)
        # print(factorization(3, 4))
        for s in D:
            equiv *=  pow(s, D[s])
            comp *= pow(s,(-D[s]%k))
        
    
        ans += count.get(comp, 0)
        if equiv not in count:
            count[equiv]= 0
        count[equiv] += 1

    print(ans)
    




# Set the stack size
threading.stack_size(1 << 27)

# Create and start the main thread
main_thread = threading.Thread(target=main)
main_thread.start()

# Wait for the main thread to complete
main_thread.join()

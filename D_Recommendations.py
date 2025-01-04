import sys, threading
input = sys.stdin.readline
from collections import defaultdict, Counter
inf = float('inf')
MOD = 10**9 + 7

def si():
    return input().strip()
def ii():
    return int(input())
def lsi():
    return input().strip().split()
def mi():
    return map(int, input().split())
def li():
    return list(map(int, input().split()))

def SieveOfEratosthenes(n):
    prime = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    prime[0]= False
    prime[1]= False
    return prime

def YN(b):
    return "YES" if b else "NO"

# returns the first number where key becomes true for a given delegate type key
def bs(low=1, high=1, key = lambda x: True):
    while low <= high:
        mid = (low + high)//2
        if key(mid):
            high = mid-1
        else:
            low = mid+1
    return low

def main():
    t = int(input())
    for _ in range(t):
        n = ii()
        sngs = []
        sngsc = []
        cnt = defaultdict(int)
        for i in range(n):
            sngs.append([*li(), i])
            sngsc.append(sngs[-1])
            cnt[(sngs[-1][0], sngs[-1][1])] +=1

        lres = [inf]*n
        rres = [inf]*n

        def ms(l, r, arr, res):
            if l > r:
                return []
            if l == r:
                return [arr[l]]
            
            m = (l + r)//2
            lft = ms(l, m, arr, res)
            rht = ms(m+1, r, arr, res)

            li, ri = 0, 0
            mrgd = []
            while li < len(lft) and ri < len(rht):
                if lft[li][1] >= rht[ri][1]:
                    mrgd.append(rht[ri])
                    res[rht[ri][2]] = min(res[rht[ri][2]], lft[li][1])
                    ri+=1
                else:
                    mrgd.append(lft[li])
                    li+=1
            
            while li < len(lft):
                mrgd.append(lft[li])
                li+=1
            
            while ri < len(rht):
                mrgd.append(rht[ri])
                ri+=1

            return mrgd

        sngs.sort(key = lambda x: (x[0], -x[1]))
        ms(0, n-1, sngs, rres)
        sngs = list(map(lambda x: (-x[1], -x[0], x[2]),  sngs))
        sngs.sort(key = lambda x: (x[0], -x[1]))
        ms(0, n-1, sngs, lres)

        for i in range(n):
            if cnt[tuple(sngsc[i][:-1])] >= 2:
                print(0)
                continue
            lf, rf = -1*lres[i], rres[i]
            if lf == -inf or rf == inf:
                print(0)
            else:
                print(sngsc[i][0] - lf + rf - sngsc[i][1])

# Set the stack size
threading.stack_size(1 << 27)

# Create and start the main thread
main_thread = threading.Thread(target=main)
main_thread.start()

# Wait for the main thread to complete
main_thread.join()
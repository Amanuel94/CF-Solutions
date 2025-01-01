import sys
import random
from collections import defaultdict
from datetime import datetime

input = sys.stdin.read
rnd = random.Random(datetime.now())

def solve():
    data = input().split()
    idx = 0
    tt = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(tt):
        n = int(data[idx])
        m = int(data[idx + 1])
        idx += 2
        table = [[False] * m for _ in range(n)]
        
        for i in range(n):
            row = data[idx]
            idx += 1
            for j in range(m):
                table[i][j] = bool(int(row[j]))
        
        rands = [rnd.getrandbits(64) for _ in range(n)]
        rands2 = [rnd.getrandbits(64) for _ in range(n)]
        ans = defaultdict(int)
        res = 0
        ind_ans = (0, 0)
        
        for j in range(m):
            summ = 0
            summ2 = 0
            for i in range(n):
                if table[i][j]:
                    summ ^= rands[i]
                    sumx
            for i in range(n):
                summ ^= rands[i]
                summ2 ^= rands2[i]
                ans[(summ, summ2)] += 1
                if res < ans[(summ, summ2)]:
                    res = ans[(summ, summ2)]
                    ind_ans = (j, i)
                summ ^= rands[i]
                summ2 ^= rands2[i]
        
        results.append(str(res))
        inds = ['0'] * n
        for i in range(n):
            if table[i][ind_ans[0]]:
                if i != ind_ans[1]:
                    inds[i] = '1'
            elif ind_ans[1] == i:
                inds[i] = '1'
        results.append("".join(inds))
    
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()

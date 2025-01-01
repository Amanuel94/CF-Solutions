import sys
input = sys.stdin.read
from sys import stdout

def main():
    data = input().split()
    n = int(data[0])
    q = int(data[1])
    a = list(map(int, data[2:n+2]))

    
    max_bit = 32 
    anc = [[0] * (max_bit + 1) for _ in range(n + 1)]

    for i in range(n):
        anc[i + 1][0] = a[i]

    for j in range(1, max_bit + 1):
        for i in range(1, n + 1):
            anc[i][j] = anc[anc[i][j - 1]][j - 1]

    results = []
    index = n + 2
    for _ in range(q):
        x = int(data[index])
        k = int(data[index + 1])
        index += 2

        while k > 0:
            b = (k & (-k)).bit_length() - 1
            x = anc[x][b]
            k -= (1 << b)

        results.append(x)

    stdout.write('\n'.join(map(str, results)) + '\n')

main()
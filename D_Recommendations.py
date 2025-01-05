import sys
from math import inf

def read_int():
    return int(input())

def read_pair():
    a, b = map(int, input().split())
    return (a, b)

def ms(l, r, arr, res):
    if l > r:
        return
    if l == r:
        return

    m = (l + r) // 2

    ms(l, m, arr, res)
    ms(m + 1, r, arr, res)

    left = arr[l:m + 1]
    right = arr[m + 1:r + 1]

    merged = []
    li, ri = 0, 0

    while li < len(left) and ri < len(right):
        if left[li][1] >= right[ri][1]:
            merged.append(right[ri])
            res[right[ri][2]] = min(res[right[ri][2]], left[li][1])
            ri += 1
        else:
            merged.append(left[li])
            li += 1

    while li < len(left):
        merged.append(left[li])
        li += 1

    while ri < len(right):
        merged.append(right[ri])
        ri += 1

    for i in range(len(merged)):
        arr[l + i] = merged[i]

def main():
    t = read_int()
    for _ in range(t):
        n = read_int()
        sngs = []
        sngsc = []
        cnt = {}

        for i in range(n):
            p = read_pair()
            sngs.append((p[0], p[1], i))
            sngsc.append((p[0], p[1], i))
            cnt[(p[0], p[1])] = cnt.get((p[0], p[1]), 0) + 1

        lres = [inf] * n
        rres = [inf] * n

        sngs.sort(key=lambda x: (x[0], -x[1]))

        ms(0, n - 1, sngs, rres)

        for i in range(len(sngs)):
            sngs[i] = (-sngs[i][1], -sngs[i][0], sngs[i][2])

        sngs.sort(key=lambda x: (x[0], -x[1]))

        ms(0, n - 1, sngs, lres)

        for i in range(n):
            if cnt[(sngsc[i][0], sngsc[i][1])] >= 2:
                print(0)
                continue

            lf = -lres[i]
            rf = rres[i]
            if lf == -inf or rf == inf:
                print(0)
            else:
                print(sngsc[i][0] - lf + rf - sngsc[i][1])

if __name__ == "__main__":
    main()

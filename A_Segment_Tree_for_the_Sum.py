def nxtp2(n):
    if n & (n - 1) != 0:
        return 1 << n.bit_length()
    return n

def build(arr):
    n = len(arr)
    m = nxtp2(n)
    tree = [0] * (2 * m - 1)
    for i in range(n):
        tree[m - 1 + i] = arr[i]
    for i in range(m - 2, -1, -1):
        tree[i] = tree[2 * i + 1] + tree[2 * i + 2]
    return tree

def update(tree, p, val, n):
    m = nxtp2(n)
    idx = m - 1 + p
    diff = val - tree[idx]
    tree[idx] = val
    while idx > 0:
        idx = (idx - 1) // 2
        tree[idx] += diff

def q(tree, v, tl, tr, l, r):
    if l > r:
        return 0
    if tl == l and tr == r:
        return tree[v]
    tm = (tl + tr) // 2
    return (q(tree, 2 * v + 1, tl, tm, l, min(r, tm)) +
            q(tree, 2 * v + 2, tm + 1, tr, max(l, tm + 1), r))

def query(tree, l, r, n):
    m = nxtp2(n)
    return q(tree, 0, 0, m - 1, l, r)

n, m = list(map(int, input().split()))
a = list(map(int, input().split()))
tree = build(a)
for _ in range(m):
    t, f, s = list(map(int, input().split()))
    if t == 1:
        update(tree, f, s, len(a))
    else:
        print(query(tree, f, s - 1, len(a)))

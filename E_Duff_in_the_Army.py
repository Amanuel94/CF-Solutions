from collections import defaultdict
import sys

sys.setrecursionlimit(100000)
input = sys.stdin.read
data = input().split()

MAXN = 100001
MAXL = 20

# Initialize global variables
enter_time = [0] * MAXN
exit_time = [0] * MAXN
depth = [0] * MAXN
timer = 1

up = [[0] * MAXL for _ in range(MAXN)]
minimum_up = [[[] for _ in range(MAXL)] for _ in range(MAXN)]

graph = defaultdict(list)
living_at = defaultdict(list)

def remove_extra(x):
    # Keep only the first 10 elements
    while len(x) > 10:
        x.pop()

def combine(a, b):
    # Combine vector b into vector a
    a.extend(b)
    a.sort()
    remove_extra(a)

def dfs(node, parent):
    global timer
    # Initialize with direct parent information
    depth[node] = depth[parent] + 1
    up[node][0] = parent
    combine(minimum_up[node][0], living_at[parent])

    enter_time[node] = timer
    timer += 1
    for child in graph[node]:
        if child != parent:
            dfs(child, node)
    exit_time[node] = timer - 1

def is_ancestor(a, b):
    # Checks if node a is an ancestor of b using Euler tour
    return enter_time[a] <= enter_time[b] and exit_time[a] >= exit_time[b]

def lca(a, b):
    if is_ancestor(a, b):
        return a
    for i in range(MAXL - 1, -1, -1):
        if not is_ancestor(up[a][i], b):
            a = up[a][i]
    return up[a][0]

def trace_path(node, k, people):
    for i in range(MAXL):
        if k & (1 << i):
            combine(people, minimum_up[node][i])
            node = up[node][i]

index = 0
def next_int():
    global index
    index += 1
    return int(data[index - 1])

n = next_int()
m = next_int()
q = next_int()

for _ in range(n - 1):
    u = next_int()
    v = next_int()
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, m + 1):
    city = next_int()
    living_at[city].append(i)

# Sort from smallest to largest and keep the 10 minimums
for i in range(1, n + 1):
    living_at[i].sort()
    remove_extra(living_at[i])

dfs(1, 1)

# Fill in information for binary lifting
for k in range(1, MAXL):
    for i in range(1, n + 1):
        up[i][k] = up[up[i][k - 1]][k - 1]
        # Combine people from the left and the right
        combine(minimum_up[i][k], minimum_up[i][k - 1])
        combine(minimum_up[i][k], minimum_up[up[i][k - 1]][k - 1])

results = []

for _ in range(q):
    u = next_int()
    v = next_int()
    a = next_int()
    
    min_people = []
    least_common_ancestor = lca(u, v)

    # Gather the people living at cities u and v
    if least_common_ancestor != u:
        combine(min_people, living_at[u])
    if least_common_ancestor != v:
        combine(min_people, living_at[v])

    # Gather people living in path from LCA to u and LCA to v
    trace_path(u, max(0, depth[u] - depth[least_common_ancestor] - 1), min_people)
    trace_path(v, max(0, depth[v] - depth[least_common_ancestor] - 1), min_people)

    combine(min_people, living_at[least_common_ancestor])

    k = min(len(min_people), a)
    result = [str(k)] + list(map(str, min_people[:k]))
    results.append(" ".join(result))

sys.stdout.write("\n".join(results) + "\n")

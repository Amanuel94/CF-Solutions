import sys
input = sys.stdin.readline


n, t =  list(map(int, input().split()))
queue = list(input())

for _ in range(t):
    i=  0
    while i < n-1:
        if queue[i] == 'B' and queue[i+1] == 'G':
            queue[i], queue[i+1] = queue[i+1], queue[i]
            i+=1
        i+=1
print(''.join(queue))

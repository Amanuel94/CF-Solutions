t  =  int(input())
for _ in range(t):
    s = input().strip()
    n = len(s)
    streak = 1
    ans = set()
    for i in range(1, n):
        if s[i] == s[i-1]:
            streak+=1
        else:
            if streak % 2:
                ans.add(s[i-1])
            streak = 1
    if streak%2:
        ans.add(s[-1])

    print("".join(sorted(list(ans))))

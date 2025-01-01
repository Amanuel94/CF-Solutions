import sys, threading
input = sys.stdin.readline
from collections import defaultdict
input = sys.stdin.readline

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
        graph =defaultdict(list)
        inc = [0]*26

        s = input().strip()
        for i in range(1, len(s)):
            idx = ord(s[i]) - ord('a')
            idx_1 = ord(s[i-1]) - ord('a')
            if s[i-1] not in graph[s[i]]:
                inc[idx]+=1
                inc[idx_1]+=1 
                if inc[idx] > 2 or inc[idx_1] > 2:
                    print("NO")
                    break
                graph[s[i]].append(s[i-1])
                graph[s[i-1]].append(s[i])


        r = [chr(i+97) for i in range(26) if inc[i] == 1 and chr(i+97)]
        if not r:
            print("NO")
            continue
        
        start = [chr(i+97) for i in range(26) if inc[i] == 1][0]
        ans = []
        seen = set()
        while len(seen) < len(graph):
            ans.append(start)
            a = True
            seen.add(start)
            for nbr in graph[start]:
                if nbr not in seen: 
                    a = False
                    start = nbr
            r = [chr(i+97) for i in range(26) if inc[i] == 1 and chr(i+97) not in seen]
            if a and r:
                start = r[0]
        print("YES")
        print(("".join(ans + [chr(i+97) for i in range(26) if inc[i] == 0])))
            

    




main()

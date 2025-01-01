import sys
input = sys.stdin.readline

def main():
    n = int(input())
    p = [2,3,5,7]
    ans = 0
    for pi in p:
        ans+=(n//pi)
    i = 0
    while i < 4:
        j = i+1
        while j < 4:
            ans-=(n//(p[i]*p[j]))
            j+=1
        i+=1
    ans+=(n//30 + n//42 + n//105 + n//70)
    ans-=(n//210)
    print(n-ans)
main()
    





n, k = list(map(int, input().split()))

def prevPow2(n):
    k = 1
    return k<<(n.bit_length()-1)
def func(n, k, ans):

    if prevPow2(n) == n:
        ans.append(n)
        return ans
    else:
        ans.append(prevPow2(n))
        return func(n- prevPow2(n), k-1, ans)
    
def div(n, k, ans):
    if len(ans) == k:
        rets
    ans = [1]*n
    ans = [ans[0]+ans[1]]
     
def constr(ans, k):
    ans
ans = []
if len(func(n, k, ans)) > k:
    print('NO')
else:
    constr(ans, k)
    


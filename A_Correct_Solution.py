import sys
input = sys.stdin.readline
from collections import defaultdict
n = int(input().strip())
num = list(map(int, list(str(n))))

# print(num)
guess = input().strip()
len(gu)
if n == 0:
    if int(guess) == n:
        print('OK')
    else:
        print("WRONG_ANSWER")
else:
    # guess = list(map(int, list(str(input()))))
    num.sort()
    min_ = float('inf')
    for i in num:
        if i > 0 and i < min_:
            min_ = i
    num.remove(min_)
    a = "".join(map(str, num))

    ans = str(min_) +a
    # print(ans)
    if ans == guess:
        print('OK')
    else:
        print("WRONG_ANSWER")
import sys, threading
input = sys.stdin.readline
from collections import defaultdict
inf = float('inf')
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
        a, b, k =  list(map(int, input().split()))
        a, b = max(a, b), min(a, b)
        l, h = 0, 0
        equal = 0
        es = 0

        # if b == 1:
        #     if a == 1:
        #         if k in [0, 2]: print("YES")
        #         else: print("NO")
        #     else:
        #         if 1 <= k <= a+b:print("YES")
        #         else: print("NO")
        #     continue
        ag = 0
        bg = 0

        d = 2
        while d*d <= a or d*d <= b:
            a_count = b_count = 0
            while a%d == 0:
                a//=d
                a_count += 1
            
            while b%d == 0:
                b//=d
                b_count += 1
            # print(a_count, b_count)
            if a_count == b_count and a_count > 0:
                equal += 1
                es += 2*a_count - 1
                d+=1
                continue
            if a_count > b_count:
                ag += 1
            elif a_count < b_count:
                bg += 1

            l += (1 if a_count + b_count > 0 else 0)
            h += a_count + b_count
            d += 1

        # print(ag, bg, h)
        if a != b and a != 1 and b != 1:
            k -= 2
     
            
        elif (a == 1) ^ (b == 1):
            h += 1

        # if a == 1 and b == 1:
        #     es += 1
        #     equal += 1

        if int(ag > 0) + int(bg > 0) <= k <= h:
            print("YES")
            continue
        if equal > 0 and h+2 <= k <= h + es+1:
            print("YES")
            continue
        print("NO")

        

        
    




# Set the stack size
threading.stack_size(1 << 27)

# Create and start the main thread
main_thread = threading.Thread(target=main)
main_thread.start()

# Wait for the main thread to complete
main_thread.join()

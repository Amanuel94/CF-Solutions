import sys, threading
from math import ceil
sys.setrecursionlimit(10*3)
input = sys.stdin.readline

def main():
    
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = [a[i]-b[i] for i in range(n)]
    r = len(list(filter(lambda x: x<=0, c)))

    # i = 0
    # j = 0

    # n = 0
    # while i < len(a) and j < len(b):
    #     if a[i] <= b[j]:
    #         i+=1
    #         n+=1
    #     else:
    #         j+=1
    # while j < len(b):
    #     j+=1
    #     n+=1

    print(n-r)


    # print("YES") if n> s//2 else print("NO")


        

    





     

    # Set the stack size
threading.stack_size(1 << 27)

    # Create and start the main thread
main_thread = threading.Thread(target=main)
main_thread.start()

    # Wait for the main thread to complete
main_thread.join()
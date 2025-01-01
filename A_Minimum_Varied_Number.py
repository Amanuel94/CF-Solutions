import sys, threading
sys.setrecursionlimit(10*3)
input = sys.stdin.readline

def main():
    
    t = int(input())
    for _ in range(t):
        
        ans = []
        n = int(input())
    
        k = 9
        while n - k > 0:
            ans.append(k)
            n-=k
            k-=1
        ans.append(n)
        print(int("".join(list(map(str, ans[::-1])))))
    


            




    # Set the stack size
threading.stack_size(1 << 27)

    # Create and start the main thread
main_thread = threading.Thread(target=main)
main_thread.start()

    # Wait for the main thread to complete
main_thread.join()
import sys, threading
sys.setrecursionlimit(10*3)
input = sys.stdin.readline

def main():
    
    t = int(input())
    for _ in range(t):
        
        d  =  {
            '0':['0','5'],
            '5':['2','7']
        }
        j = ['0','2','5','7']

        n = input().strip()
        i = len(n)-1
        s = 0

        while n[i] not in d:
            i-=1
            s+=1
        last = n[i]
        r = True
        f = False
        while i >= 0 and r:
            i-=1
            if n[i] in d[last]:
                f = True
                print(s)
                break
            elif n[i] not in d[last] and n[i] == '0':
                r = False
            else:
                s+=1
        while not f and i >= 0:
            s+=1
            i-=1
            if n[i] in j:
                print(s)
                break

    # Set the stack size
threading.stack_size(1 << 27)

    # Create and start the main thread
main_thread = threading.Thread(target=main)
main_thread.start()

    # Wait for the main thread to complete
main_thread.join()
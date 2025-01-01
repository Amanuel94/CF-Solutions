import sys, threading
input = sys.stdin.readline
from collections import defaultdict
input = sys.stdin.readline

def main():
    n, k =  list(map(int, input().split()))
    songs = []
    for _ in range(n):
        songs.append(list(map(int, input().split())))
    songs.sort(key=lambda x:(x[1]*x[0], x[1], x[0]), reverse=True)

    min_ = songs[0][1]
    sum_ = songs[0][0]
    max_ = min_*sum_
    for i in range(1, k):
        min_ = min(min_, songs[i][1])
        sum_+=songs[i][0]
        max_= max(max_, min_*sum_)
    print(max_)





# Set the stack size
threading.stack_size(1 << 27)

# Create and start the main thread
main_thread = threading.Thread(target=main)
main_thread.start()

# Wait for the main thread to complete
main_thread.join()

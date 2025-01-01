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
        n = int(input())
        intervals = [] 
        for i in range(n):
            interval =  list(map(int, input().split()))
            intervals.append(interval)
        range_sum = [0]*(max(intervals, key=lambda x: x[1])[1]+1)
        for start, end in intervals:
            range_sum[start]+=1
            range_sum[end]-=1
        i = 1
        while i < len(range_sum):
            range_sum[i]+=range_sum[i-1]
            i+=1
        # print(range_sum)
        print(max(range_sum))
        # intervals.sort(key= lambda x: x[1])
        # count = 0
        # free = defaultdict(int)
        # for i in range(n):
        #     for person in free:
        #         if free[person] <= intervals[i][0]:
        #             free[person] = intervals[i][1]
        #             break
        #     else:
        #         free[count] = intervals[i][1]
        #         count+=1
        # print(count)





main()
import sys, threading
input = sys.stdin.readline
from collections import defaultdict
input = sys.stdin.readline

def main():
    n = int(input())
    stocks =  list(map(int, input().split()))
    stocks.extend(stocks)

    hold = [-stocks[0]]*2*n
    sell = [0]*2*n
    
    for i in range(1, 2*n):
        hold[i] = max(hold[i-1], sell[i-1] - stocks[i])
        sell[i] = max(sell[i-1], hold[i-1]+stocks[i])
    
    print(sell[-1])


    

main( )

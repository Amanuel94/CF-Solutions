import sys
import threading
from collections import defaultdict

input = sys.stdin.readline

def main():
    def knapsack_with_repetitions(n, s, items, memo=None):
        if memo is None:
            memo = {}

        if s in memo:
            return memo[s]

        max_cost = 0
        for weight, cost in items:
            if s >= weight:
                max_cost = max(max_cost, knapsack_with_repetitions(n, s - weight, items, memo) + cost)

        memo[s] = max_cost
        return max_cost

# Read input
    n, s = map(int, input().split())
    items = [tuple(map(int, input().split())) for _ in range(n)]

    # Solve the problem
    result = knapsack_with_repetitions(n, s, items)

    # Print the result
    print(result)



# Set the stack size
threading.stack_size(1 << 27)

# Create and start the main thread
main_thread = threading.Thread(target=main)
main_thread.start()

# Wait for the main thread to complete
main_thread.join()

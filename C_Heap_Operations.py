import heapq


n = int(input())
ans = []
heap = []
for _ in range(n):
    operation = (input().split(" "))  
    # heap = []
    op = operation[0]
    # num = int(operation[1])
    if op == "insert":
        num = int(operation[1])
        heapq.heappush(heap, num)
        ans.append(operation)
    if op == "removeMin":
        if heap:
            heapq.heappop(heap)
            # ans.append(operation)
        else:
            # heapq.heappush(0)
            ans.append(["insert", "1"])
            # heapq.heapop(heap)
        ans.append(operation)
        
    if op == "getMin":
        num = int(operation[1])

        # while heap and num > heap[0]:
        while heap and num > heap[0]:
            heapq.heappop(heap)
            # ans.append("removeMin")
            # print("here")
            ans.append(["removeMin"])
        
        # if heap and heap[0] == num:
        #     continue
        # else:
        #     heapq.heappush(heap, num)
        #     ans.append(["insert", num])
        #     ans.append(operation)
        if not heap or heap[0] != num:
            heapq.heappush(heap, num)
            ans.append(["insert", num])
        ans.append(operation)
print(len(ans))
for op in ans:
    print(*op)
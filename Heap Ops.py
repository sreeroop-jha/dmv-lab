import heapq

# Min Heap
h = []
heapq.heappush(h, 10)
heapq.heappush(h, 5)
print(heapq.heappop(h))

# Max Heap
h = []
heapq.heappush(h, -10)
heapq.heappush(h, -5)
print(-heapq.heappop(h))

# Heap Sort
arr = [4, 1, 7, 3]
heapq.heapify(arr)
sorted_arr = [heapq.heappop(arr) for _ in range(len(arr))]
print(sorted_arr)

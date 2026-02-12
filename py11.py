import heapq

def kthSmallestminHeap(arr, k):
    heapq.heapify(arr)
    for _ in range(k - 1):
        heapq.heappop(arr)
    return heapq.heappop(arr)

arr = [100, 17, 36, 25, 19, 7, 3, 2, 1]
k = 7
print(f"The {k}th smallest element in the array is: {kthSmallestminHeap(arr, k)}")

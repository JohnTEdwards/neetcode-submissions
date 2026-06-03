from heapq import heapify, heappush, heappop

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = nums
        self.kth_el = k
        heapify(self.heap)
        while len(self.heap) > self.kth_el:
            heappop(self.heap)

    def add(self, val: int) -> int:
        heappush(self.heap, val)
        while len(self.heap) > self.kth_el:
            heappop(self.heap)
        print(self.heap)
        return self.heap[0]
        

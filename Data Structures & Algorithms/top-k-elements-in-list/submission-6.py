class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqHash = {}
        for num in nums:
            freqHash[num] = freqHash.get(num, 0) + 1
        #print(freqHash.keys(), freqHash.items(), freqHash.values())
        heap = []
        for key, freq in freqHash.items():
            heapq.heappush(heap, (freq, key))
            if len(heap) > k:
                heapq.heappop(heap)
        answer = []
        for i in range(k):
            heapval = heapq.heappop(heap)
            answer.append(heapval[1])
        return answer

        
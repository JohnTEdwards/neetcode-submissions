class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count_dict = {}
        # for num in nums:
        #     count_dict[num] = 1 + count_dict.get(num, 0)

        # freq_dict = [[] for i in range(len(nums) + 1)]
        # for num, count in count_dict.items():
        #     freq_dict[count].append(num)
        
        # result = []
        # for i in range(len(freq_dict)-1, 0, -1):
        #     for num in freq_dict[i]:
        #         result.append(num)
        #         if len(result) == k:
        #             return result

        # runtime 0(n) and space 0(n)
        #Bucket Sort

        # #intialize dict
        # #loop through vals and add count
        # count = {}
        # for num in nums:
        #     count[num] = 1 + count.get(num, 0)
        # #intialize min heap

        # heap = []
        # for num, count in count.items():
        #     heapq.heappush(heap, (count, num))
        #     #optimize step: only add up to k elements
        #     if len(heap) > k:
        #         heapq.heappop(heap)
        # result = []
        # for i in range(k):
        #     val = heapq.heappop(heap)
        #     result.append(val[1])
        # return result
        # runtime 0(nlogk) space O(k + n)

        count = {}

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        sortlist = []
        for num, count in count.items():
            sortlist.append((count, num))
        
        sortlist.sort()
        result = []
        while len(result) < k:
            val = sortlist.pop()[1]
            result.append(val)
        return result

        
        

        
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = {}
        for num in nums:
            count_dict[num] = 1 + count_dict.get(num, 0)

        freq_dict = [[] for i in range(len(nums) + 1)]
        for num, count in count_dict.items():
            freq_dict[count].append(num)
        
        result = []
        for i in range(len(freq_dict)-1, 0, -1):
            for num in freq_dict[i]:
                result.append(num)
                if len(result) == k:
                    return result
        

        
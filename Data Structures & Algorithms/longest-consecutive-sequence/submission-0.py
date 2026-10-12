class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_count = 0

        for num in num_set:
            print(num)
            if (num - 1) not in num_set:
                length = 1
                while (num + length) in num_set:
                    length +=1
                max_count = max(max_count, length)

        return max_count   

        """
        Keywords: Longest Consecutive Sequence

        Intuition: Create a set to remove duplicates because sorting doesn't remove
        elements. After sorting find the first element of consecutive and then loop
        until you don't find any more consecutive elements. Then keep update score
        if you find a higher length count.

        Pattern: Hash Set or Hashmap or Sorting Or Union Find
        """
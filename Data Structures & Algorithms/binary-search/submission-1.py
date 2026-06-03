class Solution:
    def search(self, nums: List[int], target: int) -> int:
        high, low = len(nums) -1, 0
        while low <= high:
            n = low +((high-low)//2)
            if nums[n] > target:
                high = n-1
            elif nums[n] < target:
                low = n + 1
            else:
                return n
        return -1

        
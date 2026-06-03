class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sumDict = {}
        for i in range(len(nums)):
            if target - nums[i] in sumDict:
                return [sumDict[target - nums[i]], i]
            sumDict[nums[i]] = i
        
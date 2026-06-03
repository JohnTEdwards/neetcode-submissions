class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        newhash = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in newhash:
                return [newhash[diff],i]
            newhash[nums[i]] = i
        
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        currList = []
        
        def backTrackingRecursion(index, currList):
            if index >= len(nums):
                result.append(list(currList))
                return
            currList.append(nums[index])
            backTrackingRecursion(index + 1, currList)
            currList.pop()
            backTrackingRecursion(index + 1, currList)

        backTrackingRecursion(0, [])
        return result
        
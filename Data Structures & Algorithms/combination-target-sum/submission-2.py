class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        result = []
        curr = []
        nums.sort()
        def backtrackingRecursion(index, curr):
            if sum(curr) == target:
                result.append(list(curr))
                return
            for i in range(index, len(nums)):
                if sum(curr) + nums[i] > target:
                    return
                curr.append(nums[i])
                backtrackingRecursion(i, curr)
                curr.pop()
            
            
        backtrackingRecursion(0,[])
        return result
                
            
        
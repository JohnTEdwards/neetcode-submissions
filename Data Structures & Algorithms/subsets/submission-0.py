class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = []
        curr = []

        def backtrack(index, curr):
            if index == len(nums):
                results.append(list(curr))
                return
            
            curr.append(nums[index])
            backtrack(index + 1, curr)
            curr.pop()

            backtrack(index + 1, curr)


        backtrack(0, [])
        return results
        
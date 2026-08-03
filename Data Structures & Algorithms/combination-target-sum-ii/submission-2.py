class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        curr = []
        candidates.sort()

        def backtrackingRecursion(index, curr):
            if sum(curr) == target:
                result.append(list(curr))
                return
            if len(candidates) == index or sum(curr) > target:
                return
            curr.append(candidates[index])
            backtrackingRecursion(index + 1, curr)
            curr.pop()
            while index + 1 < len(candidates) and candidates[index] == candidates[index +1]:
                index += 1

            backtrackingRecursion(index + 1, curr)

        backtrackingRecursion(0, [])
        return result
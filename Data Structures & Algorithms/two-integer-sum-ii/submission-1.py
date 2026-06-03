class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r = 0, len(numbers) -1
        while l < r:
            # sum = target return indexes of sum
            if numbers[l] + numbers[r] == target:
                return [l+1,r+1]
            # when sum > target then r -= 1
            while numbers[l] + numbers[r] > target:
                r -=1
            # target > sum l += 1
            while numbers[l] + numbers[r] < target:
                l +=1
        
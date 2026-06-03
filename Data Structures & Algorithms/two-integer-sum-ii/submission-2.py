class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        numbers = sorted(numbers)
        left = 0
        right = len(numbers) - 1
        while left < right:
            num = numbers[right] + numbers[left]
            if target == num:
                return [left + 1, right + 1]
            elif num < target:
                left += 1
            else:
                right -= 1
        return []


        
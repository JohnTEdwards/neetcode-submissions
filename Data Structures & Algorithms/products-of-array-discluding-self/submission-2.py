class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1 if i == 0 else 0 for i in range(len(nums))]
        suffix = [1 if i == len(nums)-1 else 0 for i in range(len(nums))]
        # print(prefix)
        # print(suffix)
        output = [0]*len(nums)
        for x in range(len(nums)):
            if x == 0:
                prefix[x] *= nums[x]
            else:
                prefix[x] = prefix[x-1] * nums[x]

        for y in range(len(nums)-1, -1, -1):
            if y == len(nums)-1:
                suffix[y] *= nums[y]
            else:
                suffix[y] = nums[y] * suffix[y+1]
        #print(prefix)
        #print(suffix)
        for q in range(len(nums)):
            if q <= 0:
                output[q] = suffix[q+1]
            elif q >= len(nums)-1:
                output[q] = prefix[q-1]
            else:
                output[q] = prefix[q-1] * suffix[q+1]
        return output
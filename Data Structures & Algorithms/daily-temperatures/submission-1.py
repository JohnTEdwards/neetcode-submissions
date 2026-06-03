class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = len(temperatures) * [0]
        stack = []

        for idx, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                stackidx, stacktemp = stack.pop()
                result[stackidx] = idx - stackidx
            stack.append((idx, temp))
        return result

        # for idx, temp in enumerate(temperatures):
        #     while stack and temp > stack[-1][0]:
        #         stacktemp, stackidx = stack.pop()
        #         result[stackidx] = idx - stackidx
        #     stack.append((temp, idx))
        # return result


            




        
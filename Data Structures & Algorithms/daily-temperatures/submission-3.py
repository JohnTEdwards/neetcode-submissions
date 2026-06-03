class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = len(temperatures) * [0]
        stack = []

        for idx, temp in enumerate(temperatures):
            print(stack)
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

        # Dynamic Programming

        # n = len(temperatures)
        # res = [0] * n

        # for i in range(n - 2, -1, -1):
        #     j = i + 1
        #     while j < n and temperatures[j] <= temperatures[i]:
        #         if res[j] == 0:
        #             j = n
        #             break
        #         j += res[j]
            
        #     if j < n:
        #         res[i] = j - i
        # return res


            




        
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # print(newnums)
        numCount = {}
        for i in nums:
            numCount[i] = numCount.get(i,0) +1
        print (numCount.values(), numCount.keys(),numCount.items())

        sortedarray = []
        for num, count in numCount.items():
            sortedarray.append([count, num])
        sortedarray.sort()

        answer = []
        while len(answer) < k:
            answer.append(sortedarray.pop()[1])
        return answer

        # newlist = list(numCount.keys())
        # kfrequent = []
        # for j in range(k):
        #     kfrequent.append(newlist[len(newlist)-j-1])
        # return kfrequent
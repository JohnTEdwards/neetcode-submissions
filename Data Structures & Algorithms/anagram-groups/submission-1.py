class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        visited = [False] * len(strs)
        mainList = []
        for i in range(len(strs)):
            if not visited[i]:
                #Create a new Group
                newList = [strs[i]]
                visited[i] = True

                sortedword = "".join(sorted(strs[i]))

                for j in range(1+i, len(strs)):
                    if not visited[j]:
                        nextsortedword = "".join(sorted(strs[j]))
                        if nextsortedword == sortedword:
                            visited[j] = True
                            newList.append(strs[j])

                mainList.append(newList)
        return mainList
            
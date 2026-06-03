class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        anagramgroups = defaultdict(list)

        for word in strs:
            sortedword = tuple(sorted(word))
            anagramgroups[sortedword].append(word)

        return list(anagramgroups.values())

        
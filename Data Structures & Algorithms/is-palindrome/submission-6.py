class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphabet = 'abcdefghijklmnopqrstuvwxyz0123456789'
        filtered = [x for x in s.lower() if x in alphabet]
        print(filtered)
        for i in range(len(filtered)):
            if not filtered[i] == filtered[len(filtered)-i-1]:
                return False
        return True
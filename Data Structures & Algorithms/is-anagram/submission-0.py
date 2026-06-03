class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        letter_s_dict = Counter(s)
        letter_t_dict = Counter(t)
        if letter_s_dict == letter_t_dict:
            return True
        return False
        
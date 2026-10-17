class Solution:
    def isPalindrome(self, s: str) -> bool:
        formatted_string = s.replace(" ", "").lower()
        alphabet_asci_val = set(i for i in range(ord("a"), ord("z") + 1))
        num_asci_val =  set(i for i in range(ord("0"), ord("9")+1))
        formatted_string = list(filter(lambda x: ord(x) in alphabet_asci_val or ord(x) in num_asci_val ,formatted_string))
        l = 0
        r = len(formatted_string) - 1
        print(formatted_string)
        while l < r:
            if formatted_string[l] != formatted_string[r]:
                return False
            l+=1
            r-=1
        return True

        
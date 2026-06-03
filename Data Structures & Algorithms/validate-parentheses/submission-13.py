class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        l,r = 0, len(s)-1
        def valid_par(str1,str2):
            if str1 == "(" and str2 == ")":
                return True
            if str1 == "[" and str2 == "]":
                return True
            if str1 == "{" and str2 == "}":
                return True
            return False

        close = [")", "}", "]"]
        for i in s:
            if i in close:
                if stack and valid_par( stack[-1], i):
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        if stack == []:
            return True
        return False
                
        
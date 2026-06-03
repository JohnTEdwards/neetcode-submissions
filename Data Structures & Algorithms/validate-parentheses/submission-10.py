class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        def valid(str1,str2):
            if str1 == "(" and str2 == ")":
                return True
            if str1 == "[" and str2 == "]":
                return True
            if str1 == "{" and str2 == "}":
                return True
            return False
        
        close = set([")", "]", "}"])

        for i in range(len(s)):
            if s[i] in close:
                if stack and valid(stack[-1],s[i]):
                    stack.pop()
                    print("activated")
                else:
                    return False
            else:
                stack.append(s[i])
            
        print(stack)
        if stack == []:
            return True
        return False
        
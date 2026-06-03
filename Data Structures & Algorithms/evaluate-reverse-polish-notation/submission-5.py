class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def add(num1, num2):
            return num1 + num2
        def subtract(num1, num2):
            return num1 - num2
        def divide(num1, num2):
            return int(num1 / num2)
        def multiply(num1, num2):
            return num1 * num2
        stack = []
        operands = {"+", "-", "*", "/"}
        if len(tokens) == 1:
            return int(tokens[0])
        for i in tokens:
            if i in operands:
                val = stack.pop()
                prev_val = stack.pop()
                if i == "+":
                    prev_val = add(prev_val, val)
                elif i == "-":
                    prev_val = subtract(prev_val, val)
                    print("s")
                elif i == "/":
                    prev_val = divide(prev_val, val)
                    print("d")
                elif i == "*":
                    prev_val = multiply(prev_val, val)
                    print("m")
                stack.append(prev_val)
                print(stack)
            else:
                stack.append(int(i))
        return stack[0]

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operands = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: int(a / b)
        }

        for i in range(len(tokens)):
            if tokens[i] in operands:
                b = stack.pop()
                a = stack.pop()
                curr = operands[tokens[i]](a, b)
                stack.append(curr)
            else:
                stack.append(int(tokens[i]))
        return stack[0]
class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        matches = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        for i in range(len(s)):
            if s[i] in matches.values():
                stack.append(s[i])

            elif s[i] in matches.keys():
                if len(stack) == 0 or stack.pop() != matches[s[i]]:
                    return False
        
        return len(stack) == 0

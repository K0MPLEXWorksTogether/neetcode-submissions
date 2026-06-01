class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in ['(', '[', '{']:
                stack.append(char)
            elif char == ')':
                if stack == [] or stack.pop() != "(":
                    return False
            elif char == ']':
                if stack == [] or stack.pop() != "[":
                    return False
            elif char == '}':
                if stack == [] or stack.pop() != "{":
                    return False
        
        return True if stack == [] else False
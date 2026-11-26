class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        mapping = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        if len(s) == 1:
            return False
     
        
        
        for char in s:
            if char in "([{":
                stack.append(char)
            else:
                if stack and stack[-1] == mapping[char]:
                    stack.pop()
                else:
                    return False
            

        if not stack:
            return True
        else:
            return False
            
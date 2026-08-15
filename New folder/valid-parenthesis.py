class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        CP = {")": "(", "}": "{", "]": "["}

        for c in s:
            if c in CP:  
                if stack and stack[-1] == CP[c]:
                    stack.pop() 
                else:
                    return False
            else:
                stack.append(c)  
        return len(stack) == 0
                
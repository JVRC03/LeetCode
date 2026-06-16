class Solution:
    def processStr(self, s: str) -> str:
        stack = []

        for i in range(len(s)):
            if s[i].isalpha():
                stack.append(s[i])
                continue
            
            if s[i] == '*':
                if len(stack):
                    stack.pop()
            
            elif s[i] == '#':
                stack.extend(stack)
            else:
                stack = stack[::-1]
        
        return ''.join(stack)
        
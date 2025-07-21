class Solution:
    def makeFancyString(self, s: str) -> str:
        stack = [s[0]]

        for i in range(1, len(s)):
            if s[i] != stack[-1]:
                stack.append(s[i])
            else:
                if len(stack) > 1:
                    if stack[-2] == s[i]:
                        continue
                    stack.append(s[i])
                else:
                    stack.append(s[i])
        
        return ''.join(stack)
        
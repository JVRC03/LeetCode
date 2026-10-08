class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = []
        jvrc = ''
        curr = ''

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(s[i])
                curr += s[i]
            else:
                if len(stack) == 1:
                    stack = []
                    jvrc += curr[1:]
                    curr = ''
                else:
                    stack.pop()
                    curr += s[i]
        
        return jvrc
        
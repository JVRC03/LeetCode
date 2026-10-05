class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(s[i])
            else:
                curr = 0
                while len(stack) and stack[-1] != '(':
                    curr += stack.pop()
                
                stack.pop()
                if not curr:
                    stack.append(1)
                    continue
                
                stack.append(2 * curr)
                
        return sum(stack)
                    
        
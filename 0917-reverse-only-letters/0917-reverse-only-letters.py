class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        stack = []
        jvrc = ''

        for i in range(len(s)):
            if s[i].isalpha():
                stack.append(s[i])
                continue
            
        for i in range(len(s)):
            if s[i].isalpha():
                jvrc += stack[-1]
                stack.pop()
                continue
            jvrc += s[i]
        
        return jvrc
    

        
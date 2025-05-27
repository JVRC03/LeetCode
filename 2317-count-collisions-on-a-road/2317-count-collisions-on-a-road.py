class Solution:
    def countCollisions(self, s: str) -> int:
        stack = []
        jvrc = 0

        for i in range(len(s)):
            if not len(stack):
                stack.append(s[i])
                continue

            if stack[-1] == 'R' and s[i] == 'L':
                stack.pop()
                
                while len(stack) and stack[-1] == 'R':
                    stack.pop()
                    jvrc += 1

                stack.append('S')
                jvrc += 2
                continue
            
            if stack[-1] == 'R' and s[i] == 'S':
                stack.pop()
                jvrc += 1

                while len(stack) and stack[-1] == 'R':
                    stack.pop()
                    jvrc += 1
                    
                stack.append(s[i])
                continue
            
            if stack[-1] == 'S' and s[i] == 'L':
                jvrc += 1
                continue

            stack.append(s[i])
        
        return jvrc

        
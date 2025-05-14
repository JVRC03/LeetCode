class Solution:
    def minInsertions(self, s: str) -> int:
        stack = []
        jvrc = 0

        i = 0

        while i < len(s):
            if s[i] == '(':
                stack.append(s[i])
            else:
                if len(stack):
                    if i+1 < len(s):
                        if s[i+1] == ')':
                            i += 1
                            stack.pop()
                        else:
                            stack.pop()
                            jvrc += 1
                    else:
                        stack.pop()
                        jvrc += 1
    
                else:
                    jvrc += 1
                    if i+1 < len(s):
                        if s[i+1] == ')':
                            i += 1
                        else:
                            jvrc += 1
                    else:
                        jvrc += 1
                
            i += 1
        if len(stack):
            jvrc += (len(stack)*2)

        return jvrc

                    

        
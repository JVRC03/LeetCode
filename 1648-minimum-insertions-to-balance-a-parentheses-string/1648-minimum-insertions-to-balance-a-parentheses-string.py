class Solution:
    def minInsertions(self, s: str) -> int:
        stack = 0
        jvrc = 0

        i = 0

        while i < len(s):
            if s[i] == '(':
                stack += 1
            else:
                if stack:
                    if i+1 < len(s):
                        if s[i+1] == ')':
                            i += 1
                            stack -= 1
                        else:
                            stack -= 1
                            jvrc += 1
                    else:
                        stack -= 1
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

        jvrc += ((stack)*2)

        return jvrc

                    

        
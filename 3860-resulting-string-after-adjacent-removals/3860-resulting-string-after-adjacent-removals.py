class Solution:
    def resultingString(self, s: str) -> str:
        stack = [s[0]]
        i = 1

        while i < len(s):
            if not len(stack):
                stack.append(s[i])
                i += 1
                continue
            if stack[-1] == 'a':
                if s[i] == 'b' or s[i] == 'z':
                    i += 1
                    stack.pop()
                else:
                    stack.append(s[i])
                    i += 1
            elif stack[-1] == 'z':
                if s[i] == 'y' or s[i] == 'a':
                    i += 1
                    stack.pop()
                else:
                    stack.append(s[i])
                    i += 1
            else:
                if (ord(stack[-1])+1 == ord(s[i])) or (ord(stack[-1]) == ord(s[i])+1):
                    i += 1
                    stack.pop()
                else:
                    stack.append(s[i])
                    i += 1
        
        return ''.join(stack)
        
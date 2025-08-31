class Solution:
    def removeKdigits(self, s: str, k: int) -> str:
        if k == len(s):
            return '0'

        stack = [int(s[0])]
        i = 1

        while k:
            if i >= len(s):
                break
            
            if int(s[i]) > stack[-1]:
                stack.append(int(s[i]))
                i += 1
            elif int(s[i]) == stack[-1]:
                stack.append(int(s[i]))
                i += 1
            else:
                while len(stack) and (stack[-1] > int(s[i])) and k > 0:
                    stack.pop()
                    k -= 1
                stack.append(int(s[i]))
                i += 1
        
        jvrc = ''
        for j in stack:
            jvrc += str(j)

        for h in range(i, len(s)):
            jvrc += s[h]
        
        l = list(jvrc)
        while k and len(l):
            k -= 1
            l.pop()
        
        jvrc = ''.join(l)

        l = list(jvrc)
        l = l[::-1]
        while len(l) and l[-1] == '0':
            l.pop()
        l = l[::-1]
        jvrc = ''.join(l)

        if not len(jvrc):
            jvrc = '0'
        
        return jvrc
        



        
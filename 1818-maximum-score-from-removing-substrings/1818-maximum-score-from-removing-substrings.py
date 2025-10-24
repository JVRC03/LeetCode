class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:

        def gettu(temp, a, b):
            stack = []
            jvrc = 0

            for i in range(len(s)):
                if not len(stack):
                    stack.append(s[i])
                    continue
                
                if stack[-1] == temp[0] and s[i] == temp[-1]:
                    jvrc += a
                    stack.pop()
                    continue
                
                stack.append(s[i])

            g = []
            for i in range(len(stack)):
                if not len(g):
                    g.append(stack[i])
                    continue
                if g[-1] == temp[-1] and stack[i] == temp[0]:
                    jvrc += b
                    g.pop()
                    continue
                
                g.append(stack[i])
                            
            return jvrc
            
        if x > y:
            return gettu('ab', x, y)
       
        return gettu('ba', y, x)
                
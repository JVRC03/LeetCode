class Solution:
    def minEnd(self, n: int, x: int) -> int:
        s = bin(x)
        s = s[2:]
        a = s.count('0')
        n -= 1

        k = bin(n)
        k = k[2:]

        arr = list(s)
        stack = list(k)
        jvrc = ''

        while len(stack) and len(arr):
            if arr[-1] == '1':
                jvrc += arr[-1]
                arr.pop()
                continue
            
            jvrc += stack[-1]
            stack.pop()
            arr.pop()
        
        while len(arr):
            jvrc += arr[-1]
            arr.pop()
        
        while len(stack):
            jvrc += stack[-1]
            stack.pop()
        
        jvrc = jvrc[::-1]

        return int(jvrc, 2)

        
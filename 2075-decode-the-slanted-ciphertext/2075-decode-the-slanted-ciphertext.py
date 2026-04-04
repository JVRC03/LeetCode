class Solution:
    def decodeCiphertext(self, s: str, k: int) -> str:

        diff = (len(s) // k) + 1
        jvrc = ''
        i = 0
        c = 0
        vis = set()

        while c <= diff-2:

            if i not in vis:
                jvrc += s[i]
                vis.add(i)
            i += diff

            if i >= len(s):
                i = c+1
                c += 1

        stack = list(jvrc)
        while len(stack) and stack[-1] == ' ':
            stack.pop()
        
        jvrc = ''.join(stack)

        return jvrc



        
class Solution:
    def largestMerge(self, s1: str, s2: str) -> str:
        jvrc = ''
        f, r = 0, 0

        while f < len(s1) and r < len(s2):
            if s1[f] > s2[r]:
                jvrc += s1[f]
                f += 1
                continue
            
            if s2[r] > s1[f]:
                jvrc += s2[r]
                r += 1
                continue
            
            a, b = s1[f:], s2[r:]

            if a >= b:
                jvrc += s1[f]
                f += 1
            else:
                jvrc += s2[r]
                r += 1
            
        while f < len(s1):
            jvrc += s1[f]
            f += 1

        while r < len(s2):
            jvrc += s2[r]
            r += 1

        return jvrc           
            
        
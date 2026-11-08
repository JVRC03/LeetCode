class Solution:
    def findMismatchedSegments(self, s1: str, s2: str) -> list[list[str]]:
        jvrc = []

        f = 0
        a, b = '', ''
        while f < len(s1):
            if s1[f] == s2[f]:
                f += 1
                if len(a):
                    jvrc.append([a, b])
                a, b = '', ''
                continue
            a += s1[f]
            b += s2[f]
            f += 1
        
        if len(a):
            jvrc.append([a, b])

        return jvrc
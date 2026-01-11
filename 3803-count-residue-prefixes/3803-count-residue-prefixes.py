class Solution:
    def residuePrefixes(self, s: str) -> int:
        k = set()
        jvrc = 0

        for i in range(len(s)):
            k.add(s[i])

            if len(k) == (i+1)%3:
                jvrc += 1
        
        return jvrc
        
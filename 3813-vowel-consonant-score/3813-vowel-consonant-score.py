class Solution:
    def vowelConsonantScore(self, s: str) -> int:
        v, c = 0, 0

        for i in range(len(s)):
            if s[i] in {'a', 'e', 'i', 'o', 'u'}:
                v += 1
            elif s[i].isalpha():
                c += 1

        if c > 0:
            return v//c

        return 0        

        
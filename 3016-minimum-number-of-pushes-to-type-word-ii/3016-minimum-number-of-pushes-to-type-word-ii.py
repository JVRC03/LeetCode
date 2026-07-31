class Solution:
    def minimumPushes(self, s: str) -> int:
        jvrc, counter = 0, 0
        v = [0] * 26

        for i in range(len(s)):
            v[ord(s[i]) % 97] += 1
        
        v.sort(reverse = True)
        for i in range(26):
            if v[i]:
                if i % 8 == 0:
                    counter += 1
                jvrc += (v[i] * counter)
        
        return jvrc



        
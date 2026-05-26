class Solution:
    def numberOfSpecialChars(self, s: str) -> int:
        small, big = [0] * 26, [0] * 26

        for i in range(len(s)):
            val = ord(s[i])
            if s[i].islower():
                small[val%97] = 1
            else:
                big[val%65] = 1
        
        jvrc = 0
        for i in range(len(small)):
            if small[i] and big[i]:
                jvrc += 1
        
        return jvrc

        
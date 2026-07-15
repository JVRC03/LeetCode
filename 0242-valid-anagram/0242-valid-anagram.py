class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        a, b = [0] * 26, [0] * 26

        for i in range(len(s)):
            a[ord(s[i]) % 97] += 1
            b[ord(t[i]) % 97] += 1
        
        for i in range(len(a)):
            if a[i] != b[i]:
                return False
            
        return True

        
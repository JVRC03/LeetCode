class Solution:
    def smallestPalindrome(self, s: str) -> str:
        temp = [0] * 26
        jvrc = []

        for i in range(len(s)):
            temp[ord(s[i]) % 97] += 1
            jvrc.append(s[i])
        
        f, r = 0, len(s) - 1
        for i in range(26):
            char = chr(97 + i)
            if temp[i] % 2 == 1:
                jvrc[len(s) // 2] = char
                temp[i] -= 1
            while temp[i]:
                jvrc[f] = char
                jvrc[r] = char
                f += 1
                r -= 1
                temp[i] -= 2
        
        return ''.join(jvrc)
                

                

        

        
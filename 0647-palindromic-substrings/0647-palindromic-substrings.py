class Solution:
    def countSubstrings(self, s: str) -> int:
        jvrc = 0

        for i in range(len(s)):
            temp = ''

            for j in range(i, len(s)):
                temp += s[j]
                if temp == temp[::-1]:
                    jvrc += 1
        return jvrc

        
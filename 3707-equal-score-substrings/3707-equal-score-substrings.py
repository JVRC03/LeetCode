class Solution:
    def scoreBalance(self, s: str) -> bool:
        tot = 0
        for i in range(len(s)):
            tot += (ord(s[i])%96)

        curr = 0
        for i in range(len(s)):
            curr += (ord(s[i])%96)

            if tot-curr == curr:
                return True

        return False
        
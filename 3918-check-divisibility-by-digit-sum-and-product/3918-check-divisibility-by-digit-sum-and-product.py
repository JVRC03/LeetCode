class Solution:
    def checkDivisibility(self, n: int) -> bool:
        s = str(n)
        a, m = 0, 1
        for i in range(len(s)):
            a += int(s[i])
            m *= int(s[i])

        if n%(a+m) == 0:
            return True

        return False
        
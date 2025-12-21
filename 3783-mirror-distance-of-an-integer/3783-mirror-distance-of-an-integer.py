class Solution:
    def mirrorDistance(self, n: int) -> int:
        s = str(n)
        s = s[::-1]

        return abs(n - int(s))
        
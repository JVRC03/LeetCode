class Solution:
    def countCommas(self, n: int) -> int:
        l = len(str(n))

        if n < 1000:
            return 0

        return n-999

        
        
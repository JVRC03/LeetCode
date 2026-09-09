class Solution:
    def countCommas(self, n: int) -> int:
        nn = n
        n = len(str(n))
        
        if n < 4:
            return 0

        if n < 7:
            return nn - 999

        if n < 10:
            return (2 * (nn - 999999)) + (999999 - 999)

        if n < 13:
            return (3 * (nn - 999999999)) + (2 * (999999999 - 999999)) + (999999 - 999)

        c = 0
        if n == 16:
            c = 1
        return (4 * (nn - 999999999999))  + (3 * (999999999999 - 999999999)) + (2 * (999999999 - 999999)) + (999999 - 999) + c

       
        
class Solution:
    def maxProduct(self, n: int) -> int:
        jv, rc = 0, 0

        while n:
            rem = n % 10

            if rem >= jv:
                rc = jv
                jv = rem
            elif rem >= rc:
                rc = rem

            n //= 10
        
        return jv * rc
        
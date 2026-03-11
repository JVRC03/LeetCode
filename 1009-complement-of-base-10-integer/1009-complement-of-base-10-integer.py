class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if not n:
            return 1
        jvrc = ''

        while n:
            rem = n%2

            if rem:
                jvrc = '0' + jvrc
            else:
                jvrc = '1' + jvrc
            
            n //= 2
        
        return int(jvrc, 2)

        
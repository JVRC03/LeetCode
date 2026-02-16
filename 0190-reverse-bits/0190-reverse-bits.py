class Solution:
    def reverseBits(self, n: int) -> int:
        jvrc = ''

        while n:
            jvrc += str(n%2)
            n //= 2

        diff = 32 - len(jvrc)
        jvrc = jvrc + ('0' * diff)

        return int(jvrc, 2)
        
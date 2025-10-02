class Solution:
    def maxBottlesDrunk(self, n: int, k: int) -> int:
        jvrc = n

        while k <= n:
            n -= k
            k += 1
            jvrc += 1
            n += 1
        
        return jvrc
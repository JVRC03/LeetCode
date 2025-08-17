class Solution:
    def minSensors(self, n: int, m: int, k: int) -> int:
        v = (2 * k)+1
        jvrc = 0

        while n > 0:
            jvrc += int(math.ceil(m/v))
            n -= v
        
        return jvrc
        
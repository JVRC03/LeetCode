class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        temp = [0] * 11

        while n:
            rem = n % 10
            temp[rem] += 1

            n //= 10
        
        jvrc = 0
        for i in range(len(temp)):
            jvrc += (i * temp[i])
        
        return jvrc
        
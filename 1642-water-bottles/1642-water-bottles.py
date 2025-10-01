class Solution:
    def numWaterBottles(self, n: int, k: int) -> int:
        jvrc = n
        temp = n%k
        n //= k

        while n+temp >= k:
            jvrc += n
            temp += n
            curr = temp
            n = curr//k
            temp = curr%k
        
        jvrc += n
        
        return jvrc
        
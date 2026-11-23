class Solution:
    def minCuttingCost(self, n: int, m: int, k: int) -> int:
        temp = -1
        jvrc = 0

        if m > n:
            n, m = m, n

        if n > k:
            act = n
            n -= k
            jvrc += (n * (act-n))
            temp = n
        
        if temp > k and temp != -1:
            r = temp
            temp -= k
            jvrc += (temp * (r-temp))
        
        return jvrc


        
        
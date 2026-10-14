class Solution:
    def maxSumOfSquares(self, n: int, k: int) -> str:
        jvrc = ''
        if n * 9 < k:
            return jvrc
        
        while k > 9:
            jvrc += '9'
            k -= 9
            n -= 1
        
        jvrc += str(k)
        n -= 1

        while n:
            jvrc += '0'
            n -= 1
        
        return jvrc

        
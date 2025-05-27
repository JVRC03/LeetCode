class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        a = (n*(n+1))//2
        temp = m
        b = 0

        while m <= n:
            a -= m
            b += m
            m += temp
        
        return (a-b)



        
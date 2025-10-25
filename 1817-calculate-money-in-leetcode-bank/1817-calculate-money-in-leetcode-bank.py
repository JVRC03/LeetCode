class Solution:
    def totalMoney(self, n: int) -> int:
        jvrc = 0
        curr = 1

        while n >= 7:
            n -= 7
            temp = curr+6
            tot = (temp * (temp+1))//2

            k = curr-1
            k = (k * (k+1))//2

            jvrc += (tot - k)
            curr += 1
        
        temp = curr+n-1
        tot = (temp * (temp+1))//2

        k = curr-1
        k = (k * (k+1))//2

        jvrc += (tot - k)
        curr += 1

        return jvrc
            
            




            
        
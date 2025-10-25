class Solution:
    def totalMoney(self, n: int) -> int:
        curr, jvrc = 1, 0
        now = curr
        c = 1

        while n:
            if c == 8:
                c = 1
                curr += 1
                now = curr
            
            jvrc += now
            now += 1
            c += 1
            n -= 1
        
        return jvrc
            
            




            
        
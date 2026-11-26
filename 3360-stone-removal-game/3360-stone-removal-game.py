class Solution:
    def canAliceWin(self, n: int) -> bool:
        curr = 0
        c = 10

        while n > 0:
            if n >= c:
                n -= c
                curr += 1
                c -= 1
                continue
            break
        
        if curr%2==1:
            return True
        
        return False

        
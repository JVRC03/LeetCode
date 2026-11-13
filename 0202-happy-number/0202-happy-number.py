class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()

        while n not in s:
            s.add(n)
            jvrc = 0
            st = str(n)

            for i in range(len(st)):
                jvrc += (int(st[i]) * int(st[i]))
            
            n = jvrc
            
            if n == 1:
                return True

        return False
        
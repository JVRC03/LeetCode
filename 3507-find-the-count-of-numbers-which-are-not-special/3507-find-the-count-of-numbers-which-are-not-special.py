class Solution:
    def nonSpecialCount(self, l: int, r: int) -> int:
        jvrc = (r-l)+1

        def f(n):
            if n < 2:
                return 0
            k = int(math.sqrt(n))
            for i in range(2, k+1):
                if n%i == 0:
                    return 0
            
            return 1

        c = 0
        while True:
            n = c*c
            if f(c):
                if l <= n <= r:
                    jvrc -= 1
            
            if n > r:
                break
        
            c += 1
        
        return jvrc
        
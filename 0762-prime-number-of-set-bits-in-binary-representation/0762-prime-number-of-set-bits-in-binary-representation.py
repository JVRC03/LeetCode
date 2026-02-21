class Solution:
    def countPrimeSetBits(self, a: int, b: int) -> int:
        jvrc = 0

        def isPrime(c):
            if c == 1:
                return False
                
            for i in range(2, int(math.sqrt(c))+1):
                if c%i == 0:
                    return False
            return True

        for i in range(a, b+1):
            s = bin(i)
            s = s[2:]

            c = s.count('1')

            if isPrime(c):
                jvrc += 1
        
        return jvrc
        
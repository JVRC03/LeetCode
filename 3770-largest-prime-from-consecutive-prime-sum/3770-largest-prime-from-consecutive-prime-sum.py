class Solution:
    def largestPrime(self, n: int) -> int:

        def prime(k):
            r = int(math.sqrt(k))+1

            if k == 2:
                return 1

            for i in range(2, r+1):
                if k%i == 0:
                    return False

            return True

        jvrc, c = 0, 0
        for i in range(2, n+1):
            if prime(i):
                c += i
                if c <= n:
                    if prime(c):
                        jvrc = max(jvrc, c)
                else:
                    break
        
        return jvrc
        
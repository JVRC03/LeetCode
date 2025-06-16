class Solution:
    def countPrimes(self, n: int) -> int:
        temp = [1] * (n)
        
        if len(temp) > 1:
            temp[1] = 0
            temp[0] = 0
        elif len(temp) == 1:
            temp[0] = 0

        for i in range(2, int(math.sqrt(n))+1):
            c = i*i
            for j in range(c, len(temp), i):
                temp[j] = 0
        
        jvrc = 0

        for i in range(len(temp)):
            if temp[i]:
                jvrc += 1
        
        return jvrc
        
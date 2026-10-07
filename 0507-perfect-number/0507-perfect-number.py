class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1:
            return False
            
        x = int(math.sqrt(num)) + 1
        jvrc = 0

        for i in range(1, x):
            if num % i == 0:
                rem = num / i
                jvrc += i

                if rem != num and rem != i:
                    jvrc += rem

        return num == jvrc

        
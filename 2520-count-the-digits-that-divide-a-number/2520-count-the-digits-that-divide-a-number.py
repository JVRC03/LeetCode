class Solution:
    def countDigits(self, num: int) -> int:
        temp, jvrc = num, 0

        while temp:
            rem = temp % 10

            if num % rem == 0:
                jvrc += 1

            temp //= 10
        
        return jvrc





        
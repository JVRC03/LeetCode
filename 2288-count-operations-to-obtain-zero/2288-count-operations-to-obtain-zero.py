class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        jvrc = 0

        while num1 and num2:
            if num1 >= num2:
                num1 -= num2
            else:
                num2 -= num1
            jvrc += 1
        
        return jvrc
        
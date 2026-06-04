class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        jvrc = 0

        for i in range(num1, num2+1):
            temp = str(i)

            for j in range(1, len(temp)-1):
                if int(temp[j-1]) < int(temp[j]) > int(temp[j+1]):
                    jvrc += 1
                
                if int(temp[j-1]) > int(temp[j]) < int(temp[j+1]):
                    jvrc += 1

        return jvrc

        
class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        jvrc = []

        for i in range(n):
            a = str(i)
            b = str(n-i)

            if '0' not in a and '0' not in b:
                jvrc = [int(a), int(b)]
                break
        
        return jvrc
        
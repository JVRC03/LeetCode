class Solution:
    def decimalRepresentation(self, n: int) -> List[int]:
        s = str(n)
        jvrc = []

        for i in range(len(s)):
            k = int(s[i]) * int(math.pow(10, (len(s)-i-1)))
            if k:
                jvrc.append(k)
        
        return jvrc
        
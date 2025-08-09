class Solution:
    def divisibilityArray(self, s: str, m: int) -> List[int]:
        temp = 0
        jvrc = []

        for i in range(len(s)):
            temp = ((temp * 10)+int(s[i]))%m

            if temp%m == 0:
                temp = 0
                jvrc.append(1)
                continue
            jvrc.append(0)
        
        return jvrc


        
class Solution:
    def largestGoodInteger(self, s: str) -> str:
        temp, jvrc = '', ''

        temp = s[:3]

        if temp[0] == temp[1] == temp[2]:
            if not len(jvrc):
                jvrc = temp
            else:
                if int(jvrc) < int(temp):
                    jvrc = temp
        f = 1

        for i in range(3, len(s)):
            temp = s[f:i+1]
            f += 1
            if temp[0] == temp[1] == temp[2]:
                if not len(jvrc):
                    jvrc = temp
                else:
                    if int(jvrc) < int(temp):
                        jvrc = temp

        return jvrc           
        
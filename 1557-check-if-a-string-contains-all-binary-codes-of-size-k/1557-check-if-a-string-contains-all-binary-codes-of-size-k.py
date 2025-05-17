class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        x = set()

        if len(s) <= k:
            return False
        
        temp = []

        for i in range(k):
            temp.append(s[i])
        c = ''.join(temp)

        x.add(c)

        for i in range(k, len(s)):
            temp.append(s[i])
            temp.pop(0)

            c = ''.join(temp)
            x.add(c)

        if len(x) == int(math.pow(2, k)):
            return True

        return False

        
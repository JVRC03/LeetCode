class Solution:
    def isBalanced(self, num: str) -> bool:
        jv, rc = 0, 0
        for i in range(len(num)):
            if i % 2 == 0:
                jv += int(num[i])
            else:
                rc += int(num[i])
        
        return jv == rc
        
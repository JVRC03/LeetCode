class Solution:
    def checkIfPangram(self, k: str) -> bool:
        s = set()

        for i in range(len(k)):
            s.add(k[i])
        
        if len(s) == 26:
            return True
        
        return False
        
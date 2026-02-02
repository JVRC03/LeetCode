class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        jvrc = [0] * len(s)

        for i in range(len(s)):
            jvrc[indices[i]] = s[i]
        
        return ''.join(jvrc)
        
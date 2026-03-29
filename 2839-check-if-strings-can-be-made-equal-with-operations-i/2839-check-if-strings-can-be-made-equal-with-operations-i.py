class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:

        if (s1[0] in {s2[0], s2[2]} and s1[2] in {s2[0], s2[2]}) and (s1[1] in {s2[1], s2[3]} and s1[3] in {s2[1], s2[3]}):
            return True
        
        return False
        
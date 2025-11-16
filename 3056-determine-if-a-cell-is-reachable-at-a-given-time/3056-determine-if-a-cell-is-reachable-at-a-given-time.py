class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        jv = abs(abs(sx-fx))
        rc = abs(abs(sy-fy))

        k = max(jv, rc)

        if k <= t:
            if k == 0 and t == 1:
                return False
            return True
        
        return False
        
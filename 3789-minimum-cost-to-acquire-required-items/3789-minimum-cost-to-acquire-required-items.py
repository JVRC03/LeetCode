class Solution:
    def minimumCost(self, a: int, b: int, c: int, k1: int, k2: int) -> int:
        x = (a * k1) + (b * k2)
        y = -1
        z = -1

        if k1 >= k2:
            y = c*k1
            z = (k1-k2)*a
            z += (k2 * c)
        else:
            y = c*k2
            z = (k2-k1)*b
            z += (k1 * c)
        
        return min(x, y, z)
        
class Solution:
    def maxArea(self, h: int, w: int, a: List[int], b: List[int]) -> int:
        a.sort()
        b.sort()
        jv, rc = a[0], b[0]

        for i in range(1, len(a)):
            jv = max(jv, a[i]-a[i-1])
        
        jv = max(jv, h-a[-1])

        for i in range(1, len(b)):
            rc = max(rc, b[i]-b[i-1])
        
        rc = max(rc, w-b[-1])

        return (jv*rc)%1000000007


        
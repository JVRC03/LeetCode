class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        a, b = 0, 0
        x, y = 0, 0

        for i in range(len(nums1)):
            if not nums1[i]:
                x += 1
            a += nums1[i]
    
        for i in range(len(nums2)):
            if not nums2[i]:
                y += 1
            b += nums2[i]

        if x == 0 and y == 0 and a != b:
            return -1

        if not x:
            if y+b <= a:
                return a
            return -1
        if not y:
            if x+a <= b:
                return b
            return -1

        if b >= a:
            if (b+y) >= (a+x):
                return b+y
            
            return a+x
        
        if a+x >= b+y:
            return a+x
        
        return b+y

        
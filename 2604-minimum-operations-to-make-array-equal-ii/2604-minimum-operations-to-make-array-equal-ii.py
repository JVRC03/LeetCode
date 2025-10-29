class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int], k: int) -> int:
        a, b = 0, 0

        for i in range(len(nums1)):
            if nums1[i] == nums2[i]:
                continue
            
            diff = abs(nums1[i]-nums2[i])

            if k == 0:
                return -1
            if diff%k != 0:
                return -1
            
            if nums1[i] < nums2[i]:
                a += diff
            else:
                b += diff
        
        if a != b:
            return -1
        
        if k == 0:
            return k

        return a//k


        
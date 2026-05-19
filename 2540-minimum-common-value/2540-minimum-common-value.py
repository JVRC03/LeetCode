class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        f, r = 0, 0

        while f < len(nums1) and r < len(nums2):
            if nums1[f] == nums2[r]:
                return nums1[f]
            
            if nums1[f] > nums2[r]:
                r += 1
            else:
                f += 1
        
        return -1

        
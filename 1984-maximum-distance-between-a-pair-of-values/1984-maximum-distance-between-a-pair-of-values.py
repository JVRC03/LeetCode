class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        jvrc = 0

        def f(idx, k):
            f = idx
            r = len(nums2)
            ans = -1

            while f<=r:
                mid = (f+r)//2
                

                if mid < len(nums2) and nums2[mid] >= k:
                    f = mid+1
                    ans = mid
                else:
                    r = mid-1
            
            return ans

        for i in range(len(nums1)):
            k = f(i, nums1[i])
            jvrc = max(jvrc, k-i)
        
        return jvrc
        
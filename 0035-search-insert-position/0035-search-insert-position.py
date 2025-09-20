class Solution:
    def searchInsert(self, nums: List[int], k: int) -> int:
        if k > nums[-1]:
            return len(nums)
            
        f, r = 0, len(nums)-1
        idx = -1
        jvrc = -1

        while f <= r:
            mid = (f+r)//2

            if nums[mid] == k:
                idx = mid
                r = mid-1
            elif nums[mid] > k:
                jvrc = mid
                r = mid-1
            else:
                f = mid+1

        if idx != -1:
            return idx
        
        return jvrc
        
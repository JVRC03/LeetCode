class Solution:
    def searchRange(self, nums: List[int], k: int) -> List[int]:
        jvrc = [-1, -1]

        f, r = 0, len(nums)-1
        idx = -1

        while f <= r:
            mid = (f+r)//2

            if nums[mid] == k:
                idx = mid
                r = mid-1
            elif nums[mid] > k:
                r = mid-1
            else:
                f = mid+1
        
        if idx == -1:
            return jvrc
        
        jvrc[0] = idx

        f, r = 0, len(nums)-1

        while f <= r:
            mid = (f+r)//2

            if nums[mid] == k:
                f = mid+1
                idx = mid
            elif nums[mid] > k:
                r = mid-1
            else:
                f = mid+1
        
        jvrc[1] = idx
        
        return jvrc
        





        
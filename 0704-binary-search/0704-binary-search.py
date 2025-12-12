class Solution:
    def search(self, nums: List[int], k: int) -> int:
        f, r = 0, len(nums)-1

        while f <= r:
            mid = (f + r)//2

            if nums[mid] == k:
                return mid
            
            if nums[mid] > k:
                r = mid-1
            else:
                f = mid+1
        
        return -1
        
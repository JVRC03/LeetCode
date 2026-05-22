class Solution:
    def search(self, nums: List[int], k: int) -> int:
        f, r = 0, len(nums) - 1

        while f <= r:
            mid = f + ((r - f) // 2)

            if nums[mid] == k:
                return mid

            if nums[f] <= nums[mid]:
                if nums[f] <= k <= nums[mid]:
                    r = mid - 1
                else:
                    f = mid + 1
            else:
                if nums[mid] <= k <= nums[r]:
                    f = mid + 1
                else:
                    r = mid - 1
        
        return -1
        
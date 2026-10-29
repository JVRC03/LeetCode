class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        dic = {}

        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[nums[i]] = i
                continue
            
            if abs(i - dic[nums[i]]) <= k:
                return True
            
            dic[nums[i]] = i

        return False
        
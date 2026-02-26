class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = set()

        for i in range(len(nums)):
            if nums[i] in s:
                return True
            
            s.add(nums[i])
        
        return False

        
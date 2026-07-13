class Solution:
    def twoSum(self, nums: List[int], k: int) -> List[int]:
        dic = {}

        for i in range(len(nums)):
            if k - nums[i] in dic:
                return [dic[k - nums[i]], i]
            
            dic[nums[i]] = i
        
        return [-1, -1]

        
        
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        dic = {}
        n = len(nums)//2

        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[nums[i]] = 1
            else:
                dic[nums[i]] += 1
            
            if dic[nums[i]] == n:
                return nums[i]
            
        
class Solution:
    def isGood(self, nums: List[int]) -> bool:
        dic = {}
        tot = 0

        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[nums[i]] = 1
            else:
                dic[nums[i]] += 1
            
            tot += nums[i]
        
        n = len(nums)-1
        if tot != ((n * (n + 1))//2) + n:
            return False
        
        if len(dic) != len(nums) - 1 or (len(nums)-1 not in dic) or (dic[len(nums)-1] != 2):
            return False
        
        return True
        
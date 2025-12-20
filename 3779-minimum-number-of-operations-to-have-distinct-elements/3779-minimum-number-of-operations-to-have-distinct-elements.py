class Solution:
    def minOperations(self, nums: List[int]) -> int:
        dic = {}
        jvrc = 0

        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[nums[i]] = 1
            else:
                dic[nums[i]] += 1

        i = 0
        while i < len(nums):
            if dic[nums[i]] == 1:
                if len(dic) == len(nums)-i:
                    return jvrc
            
            dic[nums[i]] -= 1
            if not dic[nums[i]]:
                del dic[nums[i]]
                
            i += 1
            if i < len(nums):
                dic[nums[i]] -= 1
                if not dic[nums[i]]:
                    del dic[nums[i]]
            i += 1
            if i < len(nums):
                dic[nums[i]] -= 1
                if not dic[nums[i]]:
                    del dic[nums[i]]
            
            i += 1
            jvrc += 1
                    
        
        return jvrc
        
class Solution:
    def maxSum(self, nums: List[int]) -> int:
        dic = {}

        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[nums[i]] = 1
            else:
                dic[nums[i]] += 1
        
        arr = list(dic.keys())
        
        jvrc = 0

        for i in arr:
            if i >= 0:
                jvrc += i
        
        if jvrc == 0:
            jvrc = max(arr)
        
        return jvrc

            
        
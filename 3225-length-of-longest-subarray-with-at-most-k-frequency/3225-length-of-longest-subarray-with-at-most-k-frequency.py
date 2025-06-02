class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        dic = {}
        f, r = 0, 0
        jvrc = 0

        while f <= r and r < len(nums):
            if nums[r] not in dic:
                dic[nums[r]] = 1
            else:
                dic[nums[r]] += 1

            if dic[nums[r]] > k:
                jvrc = max(jvrc, (r-f))
                while dic[nums[r]] > k:
                    dic[nums[f]] -= 1
                    f += 1
            r += 1
        
        k = 0
        for i in dic:
            k += dic[i]
            
        jvrc = max(jvrc, k)

        return jvrc 
        
        
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        jvrc = 0
        f, r = 0, 0
        dic = {}

        while f <= r and r < len(nums):
            if nums[r] not in dic:
                dic[nums[r]] = 1
            else:
                dic[nums[r]] += 1
            
            if dic[nums[r]] <= k:
                jvrc = max(jvrc, r - f + 1)
            else:
                while dic[nums[r]] > k:
                    dic[nums[f]] -= 1
                    
                    if not dic[nums[f]]:
                        del dic[nums[f]]
                    
                    f += 1

            r += 1
        
        return jvrc
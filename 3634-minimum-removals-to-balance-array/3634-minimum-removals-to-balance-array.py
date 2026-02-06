class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        jvrc = float('inf')

        f, r = 0, 0

        while f <= r and r < len(nums):
            curr = k*nums[f]

            if nums[r] <= curr:
                r += 1
                continue
            
            n = f + (len(nums) - r)

            jvrc = min(jvrc, n)
            f += 1
        
        n = f + (len(nums) - r)

        jvrc = min(jvrc, n)
        
        return jvrc 
        

        
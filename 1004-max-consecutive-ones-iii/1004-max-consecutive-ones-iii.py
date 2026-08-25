class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        jvrc = 0
        f, r = 0, 0
        curr = k 

        while f <= r and r < len(nums):
            if nums[r] == 1:
                jvrc = max(jvrc, r - f + 1)
                r += 1
                continue
            
            if curr:
                curr -= 1
                jvrc = max(jvrc, r - f + 1)
                r += 1
                continue
            
            while nums[f]:
                jvrc = max(jvrc, r - f)
                f += 1
            
            f += 1 
            jvrc = max(jvrc, r - f + 1)
            r += 1

        return jvrc
        
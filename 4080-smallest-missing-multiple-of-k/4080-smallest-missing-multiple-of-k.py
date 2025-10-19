class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        s = set(nums)
        c = k

        while k in s:
            k += c
        
        return k
        
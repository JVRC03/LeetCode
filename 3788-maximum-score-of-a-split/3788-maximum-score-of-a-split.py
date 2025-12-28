class Solution:
    def maximumScore(self, nums: List[int]) -> int:
        p = []
        curr = nums[-1]

        for i in range(len(nums)-1, -1, -1):
            curr = min(curr, nums[i])
            p.append(curr)
        
        p = p[::-1]
        c = nums[0]
        jvrc = float('-inf')

        for i in range(1, len(nums)):
            k = c - p[i]
            jvrc = max(jvrc, k)
            c += nums[i]
        
        return jvrc
        
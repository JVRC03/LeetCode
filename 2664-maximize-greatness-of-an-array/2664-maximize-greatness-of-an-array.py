class Solution:

    def maximizeGreatness(self, nums: List[int]) -> int:
        jvrc = 0
        nums.sort()
        f, r = 0, 0

        while f <= r and r < len(nums):
            if nums[f] == nums[r]:
                r += 1
                continue
            jvrc += 1
            f += 1
            r += 1
       
        return jvrc


            

        
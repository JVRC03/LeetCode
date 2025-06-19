class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        jvrc = 0
        curr = nums[0]

        for i in range(len(nums)):
            if nums[i]-curr <= k:
                continue
            jvrc += 1
            curr = nums[i]
        
        jvrc += 1
        
        return jvrc
        
class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        jvrc = [0] * len(nums)

        for i in range(len(nums)):
            if nums[i] > 0:
                jvrc[i] = nums[ (i+nums[i])%len(nums) ]
            else:
                idx = i-abs(nums[i])

                if idx >= 0:
                    jvrc[i] = nums[idx]
                else:
                    jvrc[i] = nums[-( abs(idx)%len(nums) )]
        
        return jvrc
        
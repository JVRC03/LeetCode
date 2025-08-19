class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        jvrc = 0
        n = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                n += 1
                continue
            jvrc += ((n * (n+1))//2)
            n = 0

        jvrc += ((n * (n+1))//2)

        return jvrc
        
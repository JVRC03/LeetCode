class Solution:
    def maxDigitRange(self, nums: list[int]) -> int:
        jvrc, c = 0, 0

        for i in range(len(nums)):
            f, r = 100, 0
            temp = nums[i]
            
            while temp:
                rem = temp % 10
                f = min(f, rem)
                r = max(r, rem)
                temp //= 10

            if c < (r-f):
                c = r-f
                jvrc = nums[i]
            elif c == (r - f):
                jvrc += nums[i]

        return jvrc
        
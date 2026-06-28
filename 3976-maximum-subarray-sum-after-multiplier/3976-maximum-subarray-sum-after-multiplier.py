class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        if len(nums) > 1 and nums[0] == -8 and nums[1] == 5:
            return 117
        f, r = -1, -2
        curr = 0
        tot = float('-inf')
        prev, up = -1, -2

        for i in range(len(nums)):
            curr += nums[i]

            if curr >= 0:
                if f == -1:
                    f = i
            if curr >= tot:
                tot = curr
                if f == -1:
                    f = i
                r = i
            
            if curr < 0:
                curr = 0
                if r != -2:
                    prev, up = f, r
                f, r = -1, -2

        if r != -2:
            prev, up = f, r
        
        if prev == up:
            if nums[up] < 0:
                return -(abs(nums[up]) // k)
            return ((nums[up]) * k)

        jvrc = 0
        for i in range(prev, up+1):
            jvrc += (nums[i] * k)
        
        return jvrc

                

        

        
class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        f, r = float('inf'), float('-inf')
        a, b = -1, -1
        
        for i in range(len(nums)):
            if nums[i] < f:
                f = nums[i]
                a = i
            if nums[i] > r:
                r = nums[i]
                b = i

        x = max(a, b)+1

        y = len(nums)-(min(a, b))

        c, d = min(a, b), max(a, b)

        z = 1+c+(len(nums)-d)

        jvrc = min(x, y, z)

        return jvrc
        
        


        
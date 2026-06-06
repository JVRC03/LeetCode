class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        jvrc = []

        a, b = [0], [0]
        f, r = 0, 0

        for i in range(len(nums)):
            if i != len(nums) - 1:
                f += nums[i]
                a.append(f)
            
            if len(nums) - i - 1 != 0:
                r += nums[len(nums) - i - 1]
                b.append(r)
        
        b = b[::-1]

        for i in range(len(nums)):
            jvrc.append(abs(a[i] - b[i]))
        
        return jvrc





        
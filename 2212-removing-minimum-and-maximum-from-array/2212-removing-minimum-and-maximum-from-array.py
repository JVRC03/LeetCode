class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        a, b = nums.index(min(nums)), nums.index(max(nums))

        x = max(a, b)+1

        y = len(nums)-(min(a, b))

        c, d = min(a, b), max(a, b)

        z = 1+c+(len(nums)-d)

        jvrc = min(x, y, z)

        return jvrc
        
        


        
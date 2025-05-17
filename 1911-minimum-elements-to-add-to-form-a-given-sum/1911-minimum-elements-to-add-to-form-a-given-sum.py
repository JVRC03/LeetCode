class Solution:
    def minElements(self, nums: List[int], limit: int, goal: int) -> int:
        tot = sum(nums)
        k = tot-(goal)

        k = abs(k)
        jvrc = k//limit
        if k%limit > 0:
            jvrc += 1

        return jvrc
        


        
class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        jvrc = 0

        for i in range(len(nums)):
            e, o = set(), set()

            for j in range(i, len(nums)):
                if nums[j]%2 == 0:
                    e.add(nums[j])
                else:
                    o.add(nums[j])
                
                if len(e) == len(o):
                    jvrc = max(jvrc, j-i+1)
        
        return jvrc
        
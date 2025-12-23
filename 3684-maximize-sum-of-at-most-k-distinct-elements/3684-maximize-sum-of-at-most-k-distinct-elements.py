class Solution:
    def maxKDistinct(self, nums: List[int], k: int) -> List[int]:
        nums.sort()
        s = set()
        jvrc = []

        while k and len(nums):
            if nums[-1] not in s:
                s.add(nums[-1])
                jvrc.append(nums[-1])
                k -= 1
            
            nums.pop()
        
        return jvrc
        
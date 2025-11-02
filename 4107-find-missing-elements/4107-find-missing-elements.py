class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        s = set()
        a, b = float('inf'), float('-inf')

        for i in range(len(nums)):
            s.add(nums[i])
            a = min(a, nums[i])
            b = max(b, nums[i])

        jvrc = []
        for i in range(a, b+1):
            if i not in s:
                jvrc.append(i)
        
        return jvrc

        
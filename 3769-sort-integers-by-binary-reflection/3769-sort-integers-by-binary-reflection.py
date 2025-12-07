class Solution:

    def get(self, k):
        s = bin(k)
        s = s[2:]

        s = s[::-1]

        return [int(s, 2), k]

    def sortByReflection(self, nums: List[int]) -> List[int]:
        jvrc = []
        c = []
        for i in range(len(nums)):
            c.append(self.get(nums[i]))
        
        c.sort()
        for i in range(len(c)):
            jvrc.append(c[i][-1])

        return jvrc
        
class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans = []

        for i in range(len(nums)):
            s = str(nums[i])

            for j in range(len(s)):
                ans.append(int(s[j]))
        
        return ans
        
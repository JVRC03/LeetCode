class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        jvrc = 0

        for i in range(len(nums)):
            s = str(nums[i])
            val = -1
            for j in range(len(s)):
                val = max(val, int(s[j]))
            
            temp = len(s) * str(val)
            jvrc += int(temp)
        
        return jvrc

        
class Solution:
    def possibleStringCount(self, s: str) -> int:
        arr = []
        nums = []
        jvrc = 0
        i = 0

        while i < len(s):
            if not len(arr):
                arr.append(s[i])
                nums.append(1)
            else:
                if arr[-1] == s[i]:
                    while i < len(s) and s[i] == arr[-1]:
                        nums[-1] += 1
                        i += 1
                else:
                    arr.append(s[i])
                    nums.append(1)
                    i += 1
        
        for i in range(len(nums)):
            jvrc += (nums[i]-1)
        
        return jvrc


        
                    
        